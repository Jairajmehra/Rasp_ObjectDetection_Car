from flask import Flask, render_template, request
from StoreSearchClass import store_Search
import os
dirpath = os.getcwd()
LocationToSearch = os.path.join(dirpath, 'static')
storesystem = store_Search(LocationToSearch)
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