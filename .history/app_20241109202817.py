from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import subprocess
from user_class import User

def get_disk_uuid():
    result = subprocess.run(["diskutil", "info", "/"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    for line in output.splitlines():
        if "Volume UUID" in line:
            return line.split(":")[-1].strip()
    return None


def get_courses(): #retrieves course list 
    with open('course_list.txt', 'r') as file:
        courses = file.readlines()
    return courses

user_name = User()


app = Flask(__name__)

@app.route('/') #home route 

def index():
    system_id = get_disk_uuid()

    return render_template('index.html',system_id=system_id)
 #flask knows to look for this


# Course page (new route)
@app.route("/course", methods=["POST", "GET"])
def course():
    dropdown_options = get_courses()
    if request.method == "POST":
        selected_course = request.form.get("dropdown")
        return redirect(url_for("roles", course=selected_course))
    return render_template("course.html", options=dropdown_options)

# Roles page
@app.route("/roles", methods=["POST", "GET"])
def roles():
    selected_course = request.args.get("course")
    dropdown_options = ["Role 1", "Role 2", "Role 3", "Role 4"]
    if request.method == "POST":
        selected_role = request.form.get("dropdown")
        return redirect(url_for("status", course=selected_course, role=selected_role))
    return render_template("roles.html", options=dropdown_options, selected_course=selected_course)

# Status page
@app.route("/status", methods=["POST", "GET"])
def status():
    selected_course = request.args.get("course")
    selected_role = request.args.get("role")
    dropdown_options = ["Status 1", "Status 2", "Status 3", "Status 4"]
    if request.method == "POST":
        selected_status = request.form.get("dropdown")
        return redirect(url_for("location", course=selected_course, role=selected_role, status=selected_status))
    return render_template("status.html", options=dropdown_options, selected_course=selected_course, selected_role=selected_role)

# Location page
@app.route("/location", methods=["POST", "GET"])
def location():
    selected_course = request.args.get("course")
    selected_role = request.args.get("role")
    selected_status = request.args.get("status")
    dropdown_options = ["Location 1", "Location 2", "Location 3", "Location 4"]
    if request.method == "POST":
        selected_location = request.form.get("dropdown")
        return redirect(url_for("display", course=selected_course, role=selected_role, status=selected_status, location=selected_location))
    return render_template("location.html", options=dropdown_options, selected_course=selected_course, selected_role=selected_role, selected_status=selected_status)

# Display page
@app.route("/display", methods=["GET"])
def display():
    selected_course = request.args.get("course")
    selected_role = request.args.get("role")
    selected_status = request.args.get("status")
    selected_location = request.args.get("location")
    return render_template("display.html", course=selected_course, role=selected_role, status=selected_status, location=selected_location)

if __name__ == "__main__":
    app.run(debug=True)

    