from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from databasefunctions import *
from user_class import User


def get_courses(): #retrieves course list 
    with open('course_list.txt', 'r') as file:
        courses = file.readlines()
    return courses

user = User() #instance of user class 


app = Flask(__name__)

@app.route('/') #home route 
def index():
     
    return render_template('index.html')
 #flask knows to look for this

# Course page (new route)
@app.route("/course", methods=["POST", "GET"])
def course():
    username = request.form.get('username')
    user.usernameUpdate(username)

    return render_template('course.html', username=username)

@app.route('/display', methods=['POST'])
def display():
    # Retrieve the form data
    course = request.form.get('course')
    role = request.form.get('role')
    username = user.returnUsername()
    location_enabled = 'Yes' if request.form.get('location-toggle') else 'No'
    address = request.form.get('address') 
    print(f"Course: {course}")
    print(f"Role: {role}")
    print(f"Username: {username}")
    print(f"Location Enabled: {location_enabled}")
    print(f"Address: {address}")
    # Pass all variables to the template
    return render_template('display.html', course=course, role=role, username=username, location_enabled=location_enabled, address=address)

# # Roles page
# @app.route("/roles", methods=["POST", "GET"])
# def roles():
#     selected_course = request.args.get("course")
#     dropdown_options = ["Role 1", "Role 2", "Role 3", "Role 4"]
#     if request.method == "POST":
#         selected_role = request.form.get("dropdown")

#         user.roleUpdate(selected_role)

#         return redirect(url_for("status", course=selected_course, role=selected_role))
#     return render_template("roles.html", options=dropdown_options, selected_course=selected_course)

# # Status page
# @app.route("/status", methods=["POST", "GET"])
# def status():
#     selected_course = request.args.get("course")
#     selected_role = request.args.get("role")
#     dropdown_options = ["Status 1", "Status 2", "Status 3", "Status 4"]
#     if request.method == "POST":
#         selected_status = request.form.get("dropdown")

#         user.statusUpdate(selected_status)

#         return redirect(url_for("location", course=selected_course, role=selected_role, status=selected_status))
#     return render_template("status.html", options=dropdown_options, selected_course=selected_course, selected_role=selected_role)

# # Location page
# @app.route("/location", methods=["POST", "GET"])
# def location():
#     selected_course = request.args.get("course")
#     selected_role = request.args.get("role")
#     selected_status = request.args.get("status")
#     dropdown_options = ["Location 1", "Location 2", "Location 3", "Location 4"]
#     if request.method == "POST":
#         selected_location = request.form.get("dropdown")

#         user.locationUpdate(selected_location)

#         return redirect(url_for("display", course=selected_course, role=selected_role, status=selected_status, location=selected_location))
#     return render_template("location.html", options=dropdown_options, selected_course=selected_course, selected_role=selected_role, selected_status=selected_status)

'''# Display page
@app.route("/display", methods=["GET"])
def display():

    selected_course = user.returnCourse()
    selected_role = user.returnRole()
    selected_status = user.returnStatus()
    selected_location = user.returnLocation()
    return render_template("display.html", course=selected_course, role=selected_role, status=selected_status, location=selected_location)'''

if __name__ == "__main__":
    app.run(debug=True)

    