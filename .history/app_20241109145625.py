from flask import Flask , render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import platform

app = Flask(__name__)

@app.route('/') #home route 

def index():
    system_id = platform.node()
    return render_template('index.html',system_id=system_id) #flask knows to look for this

if __name__ == '__main__':
    app.run(debug = True)