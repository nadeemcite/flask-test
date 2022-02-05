from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    question = request.args.get("question")
    if question:
        answer = "Answer"
    return render_template("index.html", question=question, answer=answer)
