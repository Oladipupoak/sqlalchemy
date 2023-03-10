from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Table, MetaData   # <--- here
from sqlalchemy.orm import sessionmaker
from database import Students,engine,Base,Session,Course,Instructor,StudentCourse
DEFAULT_FILE = "sqlite:///database.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DEFAULT_FILE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/dash", methods=("GET", "POST"))
def dash():
    return render_template("dash.html")
#students section
@app.route('/students', methods=['POST','GET'])
def students():
    return(render_template('students.html'))


@app.route('/add_student', methods=['POST'])
def add_student():
    student_name = request.form['student_name']
    email = request.form['email']
    student = Students(student_name=student_name, email=email)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_student_course', methods=['POST'])
def add_student_course():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    student_course = StudentCourse(student_id=student_id, course_id=course_id)
    db.session.add(student_course)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/students_all')
def all_students():
    students = Students.query.all()
    return render_template('students_all.html', students=students)

@app.route('/student_course')
def student_course():
    student_course = StudentCourse.query.all()
    return render_template('student_course.html', student_course=student_course)



@app.route('/add_course', methods=['POST'])
def add_course():
    course_name = request.form['course_name']
    course = Course(course_name=course_name)
    db.session.add(course)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_instructor', methods=['POST'])
def add_instructor():
    instructor_name = request.form['instructor_name']
    course_id = request.form['course_id']
    instructor = Instructor(instructor_name=instructor_name, course_id=course_id)
    db.session.add(instructor)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/courses_all')
def courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)


@app.route('/instructors_all')
def instructors():
    instructors = Instructor.query.all()
    return render_template('instructors.html', instructors=instructors)




if __name__ == '__main__':
    app.run(debug=True)



