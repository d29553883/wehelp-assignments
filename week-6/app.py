
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import session
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="website",
)
mycursor = mydb.cursor()

app=Flask(__name__,static_folder="static", static_url_path="/")

app.secret_key="asdgewrwjghjyrirjj"
@app.route("/")
def index():
    return render_template("index.html")

   

@app.route("/signup", methods=["POST"])
def signup():
    userName = request.form["username"]
    sql = "SELECT username FROM member WHERE username = %s"
    adr = (userName, )
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    if myresult != [] :
        return redirect("/error/?message=帳號已經被註冊")
    else:
        Name = request.form["name"]
        userName = request.form["username"]
        passWord = request.form["password"]
        mycursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)",(Name, userName, passWord))
        mydb.commit()
        return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    
    userName = request.form["username"]
    passWord = request.form["password"]
    print(userName)
    print(passWord)
    sql = "SELECT username,password FROM member WHERE username = %s AND password = %s"
    adr = (userName,passWord, )
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    print(myresult)    
    if myresult != [] :
        session["userName"]= userName
        username = request.form["username"]
        sql2 = "SELECT name FROM member WHERE username = %s"
        adr2 = (username,)
        mycursor.execute(sql2, adr2)
        myresult = mycursor.fetchall()
        x = myresult[0]
        x.__str__()
        session['name']= x[0] 
        print(session['name']) 
        return redirect("/member/")
    elif userName == "" or passWord =="":
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

@app.route("/error/")
def fail():
    message = request.args.get("message","請輸入帳號、密碼")
    return render_template("error.html",message=message)

@app.route("/member/")
def member():
    if "userName" in session :
        name = session['name'] 
        return render_template("member.html",name=name)
    else:
        return redirect("/") 

@app.route("/logout/")
def logout():
    del session["userName"]
    del session['name']
    return redirect("/")




if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
