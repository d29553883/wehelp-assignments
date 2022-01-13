import urllib.request as req
import json
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with req.urlopen(url) as response:
    data=json.load(response)


x = data["result"]["results"]
with open("data.csv","w", encoding="utf-8") as file:
     for landmark in x:
         file.write(landmark["stitle"]+","+(landmark["address"])[5:8]+","+landmark["longitude"]+","+landmark["latitude"]+","+"https"+((landmark["file"]).split("https"))[1]+"\n")

