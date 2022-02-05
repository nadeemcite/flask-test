from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    question = request.args.get("question")
    if question:
        answer = "Answer"
    else:
        answer = ""
    return render_template("index.html", question=question, answer=answer)
