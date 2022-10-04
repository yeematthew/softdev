'''
Matthew Yee
SoftDev
k07 -- Flask module
2022-10-4
time spent: 1 hour
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. I have seen similar syntax in Java, where functions are called using parentheses
to indicate what the arguments of a function being called are, and where an object can
be set to the results of that function being called.
1. '/' in app.route could be referring to the root directory, specifically, the highest
directory which I have access to.
2. I guessed that the print statement would somehow print to the root directory based on
the fact that the route pointed there, but that seemed unlikely to me because I wasn't sure
how that would even work.
3. The print statement would print the results of running app.
4. Yes, "No hablo queso!" would have to appear somewhere, because it is the result of
running app, and that result gets printed. However, I do not know why it prints to the browser, or how it relates to the root
directory.
5. I may have seen similar constructs in html, but my memory of the language is foggy.
...
INVESTIGATIVE APPROACH:
We compared our knowledge of APCS, NextCS, and Systems to try to piece together what some
of the syntax and symbols meant in the context of this program. Specifically, I used the
word "route" to determine that '/' had to stand for some kind of location, so I determined
it must be the root directory.
My partner and I both knew that for Q0, Flask had to be some kind of function, but we were
unsure as to what it did, or how it releated to the root directory.
'''
