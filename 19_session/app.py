#Flying Karate Masters: Matthew Yee, Kevin Li, Joseph Wu
#SoftDev
#K19 -- Cookies
#2022-11-03
#time spent: 0.2 hours

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
import redirect #TEST THIS

from flask import session

app = Flask(__name__)    #create Flask object

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

'''
#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

app.secret_key = Flask.secret_key

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    #print("***DIAG: request.args ***")
    #print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    
    print(session)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    print("***REQUEST FORM***")
    print(request.form)
    if (request.method == 'GET'):
        return render_template('response.html', username = request.args['username'], method = 'GET')
    else:
        return render_template('response.html', username = request.form['username'], method = 'POST')

'''

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

