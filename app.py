from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["planner"]
tasks = db["tasks"]


@app.route("/")
def index():

    data = list(tasks.find())

    week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    completed = 0

    for t in data:
        week[t["day"]].append(t)

        if t["done"]:
            completed += 1

    progress = 0
    if len(data) > 0:
        progress = int((completed/len(data))*100)

    return render_template(
        "index.html",
        week=week,
        progress=progress
    )


@app.route("/add", methods=["POST"])
def add():

    title = request.form["title"]
    day = request.form["day"]

    tasks.insert_one({
        "title": title,
        "day": day,
        "done": False
    })

    return redirect("/")


@app.route("/toggle/<title>")
def toggle(title):

    task = tasks.find_one({"title": title})

    tasks.update_one(
        {"title": title},
        {"$set": {"done": not task["done"]}}
    )

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
