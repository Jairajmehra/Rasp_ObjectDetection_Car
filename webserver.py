from flask import Flask, render_template, request
from ImageClass import StoreSystem
import os
dirpath = os.getcwd()
LocationToSearch = os.path.join(dirpath, 'static')
storesystem = StoreSystem(LocationToSearch)
app = Flask(__name__)

@app.route("/")
def HomePage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_data():
    user_search = request.form["user_search"]
    items = storesystem.search(user_search)
    if(items):
        return render_template('index.html',items=items)
    else:
        return "Nothing Found 404"


app.run(debug=True)