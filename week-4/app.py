
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import session

app=Flask(__name__,static_folder="static", static_url_path="/")

app.secret_key="asdgewrwjghjyrir"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    userName = request.form["username"]
    passWord = request.form["password"] 
    if userName == "test" and passWord =="test":
        session["userName"]= userName
        session["passWord"]= passWord
        return render_template("member.html")
    elif userName == "" or passWord =="":
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

@app.route("/error/")
def fail():
    message = request.args.get("message","請輸入帳號、密碼")
    return render_template("error.html",message=message)

@app.route("/member/")
def success():
    if session["userName"] in session and session["passWord"] in session:
        return render_template("member.html")
    elif not session["userName"]in session or session["passWord"] in session:
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

@app.route("/logout/")
def logout():
    session.pop('userName', None)
    session.pop('passWord', None)
    redirect("/")


app.run(port=3000)