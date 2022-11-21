#Flying Karate Masters: Matthew Yee, Jeremy Kwok, David Chen
#SoftDev
#K20 -- REST APIs
#2022-11-21
#time spent: ? hours

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return app.redirect(app.url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    form_keys = request.form.keys()
    print(request.form)