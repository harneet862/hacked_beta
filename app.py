from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from databasefunctions import *
from user_class import User


user = User() #instance of user class 


app = Flask(__name__)

@app.route('/') #home route 
def index():
    setup_db()
    return render_template('index.html')
 #flask knows to look for this

# Course page (new route)
@app.route("/course", methods=["POST", "GET"])
def course():
    #do a check here if the user already exists in database. if the user exists, go straight to display page, with settings 
    #user_list = get_all_usernames()
    # print(user_list)
    
    username = request.form.get('username')
    user.usernameUpdate(username)
    
    # if username in user_list: #if user exists
    #     return redirect(url_for('display')) # go to display page, display user details 
    # else:

    #     user.usernameUpdate(username)

    return render_template('course.html', username=username)

@app.route('/display', methods=['POST'])
def display():
    # Retrieve form data
    course = request.form.get('course')
    role = request.form.get('role')
    address = request.form.get('address')
    
    # Get user-specific data
    username = user.returnUsername()  # Assuming you have a user object with methods
    status = user.returnStatus()
    location_enabled = 'Yes' if request.form.get('location-toggle') else 'No'
    
    # Add the user (assuming add_user() is a function that inserts into the database)
    add_user(username, role, status, course, address)
    
    # Get matching users based on course, role, and status
    matches = get_users_by_course_role_and_status(course, role, status)
    
    # Render the template with all the data
    return render_template('display.html', 
                           course=course, 
                           role=role, 
                           username=username, 
                           location_enabled=location_enabled, 
                           address=address, 
                           matches=matches)

if __name__ == "__main__":
    app.run(debug=True)

    