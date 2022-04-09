from flask import Flask, session

app = Flask(__name__)

app.secret_key = "Hiya folks this is my survey site!"