from flask import Flask , render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)

@app.route('/') #home route 

def index():
    system_id = uuid.uuid1()
    course_options = ['class1','class2','class3','class4','class5']
    return render_template('index.html',system_id=system_id, options = course_options) #flask knows to look for this

if __name__ == '__main__':
    app.run(debug = True)