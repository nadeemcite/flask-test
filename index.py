from flask import Flask, render_template, request
import os
import openai

app = Flask(__name__)


@app.route('/')
def home():
    question = request.args.get("question")
    if question:
        answer = "Answer"
    else:
        openai.organization = "org-aiO2YqmcjKmGasfKm8oo8GYN"
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.Engine.list()
        resp = openai.Completion.create(
            engine="text-davinci-001",
            prompt=question,
            max_tokens=5
        )
        print(resp["choices"])
        print(resp["choices"][0])
        if resp["choices"]:
            print(resp["choices"][0]["text"])
            answer = resp["choices"][0]["text"]
        else:
            answer = "Not found any answer"
    return render_template("index.html", question=question, answer=answer)
