from flask import Flask, render_template, url_for, request, send_from_directory
from feedback_form import FeedbackForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '15e217f68d01b2bc4465fd26e8877bc4'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

gc1_test_things = [("GC thing " + str(i+1)) for i in range(7)]

@app.route("/GC1")
def GC1():
    return render_template('subjects/GC1.html', title = 'Gen Chem 1', page_vars = gc1_test_things)

oc1_test_things = [("OC thing " + str(i+1)) for i in range(7)]

@app.route("/OC1")
def OC1():
    return render_template('subjects/OC1.html', title = 'Organic Chem 1', page_vars = oc1_test_things)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

GC1M1Qs = [("Question " + str(i+1)) for i in range(10)]

@app.route("/GC1_m1")
def GC1_m1():
    return render_template('modules/GC1/M1.html', title = 'GC1 M1', qlist = GC1M1Qs)

@app.route("/GC1_m1_q1")
def GC1_m1_q1():
    return render_template('questions/GC1/M1/Q1.html', title = 'GC1 M1 Q1')

@app.route("/GC1_m1_a1")
def GC1_m1_a1():
    return render_template('answers/GC1/M1/A1.html', title = 'GC1 M1 A1')

@app.route("/testform", methods=('GET', 'POST'))
def testform():
    form = FeedbackForm()
    return render_template("forms/test.html", title = 'testform', form = form)




if __name__ == '__main__':
    app.run(debug=True)
