import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'


# ex https://Toni880:ghp_147bkkabcdefgh@github.com/Toni880/CybrogBot

os.system("git clone https://github.com/darmazi/mazirobot/ && cd Mazi && pip3 install -r requirements.txt && bash start")
