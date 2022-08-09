from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

@app.route("/")
def form():
	return render_template("form.html")

@app.route("/login", methods = ['POST', 'GET'])
def login():
	if request.method == "GET":
		return "Login via the login form"

	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']

		# database connection
		connection = pymysql.connect(
			host="localhost", 
			user="root", 
			password="", 
			database="sql_injection_db"
			)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'" )
		record = cursor.fetchone()

		if record:
			message = username + " logged in successfully"
		else:
			message = "User not found!"
		# close db connection
		connection.close()
		return message
