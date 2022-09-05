from flask import Flask, render_template, request, url_for, redirect
from bson.objectid import ObjectId

from flask_pymongo import PyMongo, pymongo
from pymongo import MongoClient
import ssl
import pprint




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

@app.route('/modify_student_details')
def modify_student_details():
 
    return render_template('modify_student_details.html')

@app.route('/view_student_details')
def view_student_details():
    return render_template('view_student_details.html')


@app.route('/delete_student_details')
def delete_student_details():
    return render_template('delete_student_details.html')      




client = MongoClient("mongodb+srv://Rajangahlout:Capg12345@cluster0.p6ksttg.mongodb.net/?retryWrites=true&w=majority", connect=False)


db = client.javatpoint

# Creating document

employees = db.employees


@app.route('/post_student_details', methods=('GET', 'POST'))
def post_student_details():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        employees.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('thanks_submittion'))

   # all_todos = employees.find_one()
    return render_template('post_student_details.html')
    
@app.route('/thanks_submittion')
def thanks_submittion():
    return render_template('thanks_submittion.html') 


if __name__ == "__main__":
   app.run(debug=True, port=8000)



