from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from databasefunctions import *
from user_class import User


user = User() #instance of user class 


app = Flask(__name__)

@app.route('/') #home route 
def index():
    return render_template('index.html')
 #flask knows to look for this

# Course page (new route)
@app.route("/course", methods=["POST", "GET"])
def course():
    #do a check here if the user already exists in database. if the user exists, go straight to display page, with settings 
    user_list = get_all_usernames()
    print(user_list)
    
    username = request.form.get('username')
    user.usernameUpdate(username)

    if username in user_list: #if user exists
        return redirect(url_for('display')) # go to display page, display user details 

    

    return render_template('course.html', username=username)

@app.route('/display', methods=['POST'])
def display():
    #need to refresh location?
    #can we add a status button 

    course = request.form.get('course')
    role = request.form.get('role')
    username = user.returnUsername()
    location_enabled = 'Yes' if request.form.get('location-toggle') else 'No'
    address = request.form.get('address') 
    status = user.returnStatus()

    # print(f"Course: {course}")
    # print(f"Role: {role}")
    # print(f"Username: {username}")
    # print(f"Location Enabled: {location_enabled}")
    # print(f"Address: {address}")
    
    # Pass all variables to the template
    add_user(username, course, role, status,address)
    return render_template('display.html', course=course, role=role, username=username, location_enabled=location_enabled, address=address)

if __name__ == "__main__":
    app.run(debug=True)

    