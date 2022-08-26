import collections
from urllib.parse import quote_plus
import ssl
from flask import Flask, render_template
from flask_pymongo import PyMongo, pymongo
from pymongo import MongoClient




app = Flask(__name__)

@app.route('/')
def Home():
 
    return render_template('index.html')

@app.route('/Admin')
def Admin():
    return render_template('Admin.html')

@app.route('/Student')
def Student():
    return render_template('Student.html')    



if __name__ == "__main__":
   app.run(debug=True, port=8000)




