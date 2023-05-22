import requests
from flask import Flask, render_template, request, redirect

import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db", user=
"postgres",password=
"tchad235", host=
"localhost",port=
"5432")

cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return  render_template('login.html')



@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        if request.form.get("login"):
            username = request.form.get('username')
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())

            if username == '' and password == '':
                return render_template('login.html', error="Username and Password must not be empty")
            elif len(records) == 0:
                return render_template('login.html', error='Username not found or incomplete details. Please try again.')
            else:
                return render_template('account.html', full_name=records[0][1], login=records[0][2],
                                       password=records[0][3])


        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html')


