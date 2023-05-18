import flask
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


def write_to_file(data):  # function is used to create a database where form info will be saved
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter='|', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # the '.to_dict() will turn the form data grabbed into a dictionary
            write_to_csv(data)  # writing the submitted forms data to the database
            return redirect('/templates/thankyou.html')  # This will be used to redirect to thankyou page after
            # a successful form submission
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong try again'


# Normal routing - navigating through pages - linking pages
# @app.route('/templates/index.html')
# def home():
#     return render_template('index.html')
#
#
# @app.route('/templates/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/templates/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/templates/works.html')
# def works():
#     return render_template('works.html')


# Dynamic routing - do the same thing as above with lesser lines of code - this will do what all 4 route are meant to do

@app.route('/templates/<page_name>')
def html_page(page_name):
    return render_template(page_name)


app.run()
