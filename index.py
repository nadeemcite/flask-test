from flask import Flask, render_template, request
import os
import openai
import pyfiglet

app = Flask(__name__)


@app.route('/')
def home():
    question = request.args.get("question")
    if not question:
        answer = ""
        question = ""
    else:
        try:
            openai.organization = "org-aiO2YqmcjKmGasfKm8oo8GYN"
            openai.api_key = os.getenv("OPENAI_API_KEY")
            openai.Engine.list()
            resp = openai.Completion.create(
                engine="text-davinci-001",
                prompt=question,
                max_tokens=10
            )
            if resp["choices"]:
                answer = resp["choices"][0]["text"]
            else:
                answer = "Not found any answer"
        except Exception as e:
            print(e)
    return render_template("index.html", question=question, answer=answer)

@app.route("/figlet")
def figlet_page():
    text = request.args.get("question")
    result = ""
    if text:
        result = pyfiglet.figlet_format(text)
    return render_template("figlet.html", result=result)