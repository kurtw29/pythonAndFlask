from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key='areyouKiddingme?'

# Password should be more than 8 characters
# Email should be a valid email
# Password and Password Confirmation should match

@app.route('/')
def regForm():
    return render_template('regFormVal.html')

@app.route('/process', methods=['post'])
def process():
    session = request.form
    for key, i in request.form.items():
        if len(i) == 0:
            flash("\"{}\" cannot be blank, you must enter ALL of your soul before continuing.".format(key), 'required')
    name_regex = re.compile(r'^[a-zA-Z\D.+_-]+$')
    if not name_regex.match(request.form['first_name']):
        flash('\"First name\" cannot contain any numbers', 'error_fname')
    if not name_regex.match(request.form['last_name']):
        flash('\"Last name\" cannot contain any numbers', 'error_lname')
    if not len(request.form['password']) > 8:
        flash("\"password\" should be more than 8 characters", 'error_pw')
    if not request.form['password'] == request.form['confirmPassword']:
        flash("\"Password\" and \"Password Confirmation\" should match", 'error_cpw')
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not email_regex.match(request.form['email']):
        flash("\"email\" invalid", error_email = )

    print(session)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)