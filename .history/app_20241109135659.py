from flask import Flask , render_template, redirect

app = Flask(__name__)

@app.route('/') #home route 

def index():
    return render_template('index.html') #flask knows to look for this

if __name__ == '__main__':
    app.run(debug = True)