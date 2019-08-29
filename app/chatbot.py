import aiml
import os
from flask import Flask, request, render_template

app = Flask(__name__)
kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = ".\startup\std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    while True:
        message= request.args.get('msg')
        if message == "quit":
            exit()
        elif message == "save":
            kernel.saveBrain("bot_brain.brn")
        else:
            bot_response = kernel.respond(message)
            return bot_response
    
