from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import bcrypt 

app = Flask(__name__)

db_config = {
    "host": "localhost:3306",
    "user": "root",
    "password": "abhijeetbi$en3",
    "database": "registration_db"
}

def connect_to_database():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route("/")
def register_form():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    connection = connect_to_database()
    cursor = connection.cursor()

    student_name = request.form["student_name"]
    father_name = request.form["father_name"]
    mother_name = request.form["mother_name"]
    phone_number = request.form["phone_number"]
    email = request.form["email"]
    date_of_birth = request.form["date_of_birth"]
    address = request.form["address"]
    blood_group = request.form["blood_group"]
    department = request.form["department"]
    course = request.form["course"]

    hashed_password = bcrypt.hashpw(request.form["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    sql = """
    INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, hashed_password))
    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for("register_form"))

if __name__ == "__main__":
    app.run(debug=True)
