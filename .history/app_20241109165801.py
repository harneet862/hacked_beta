from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import uuid


def get_courses(): #retrieves course list 
    with open('course_list.txt', 'r') as file:
        courses = file.readlines()
    return courses

app = Flask(__name__)

@app.route('/') #home route 

def index():
    system_id = uuid.uuid1()
    course_options = get_courses()
    return render_template('index.html',system_id=system_id, options = course_options)
 #flask knows to look for this

@app.route("/result", methods=["POST"])
def result():
    # Get the selected option from the form
    selected_option = request.form.get("dropdown")
    return render_template("result.html", selected_option=selected_option)


if __name__ == '__main__':
    app.run(debug = True)