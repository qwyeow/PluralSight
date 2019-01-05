from flask import Flask, render_template, redirect, url_for, request

from students import Student

student_list = []

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def student_page():
    if request.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        #new_student = Student(student_name = new_student_name, student_id = new_student_id)
        new_student = Student(student_name = new_student_name, 
                                student_id = new_student_id,
                                student_lastname = new_student_last_name)
        student_list.append(new_student)
        return redirect(url_for("student_page"))

    return render_template("index.html", students = student_list)

if __name__ == "__main__":
    app.run()    
    


