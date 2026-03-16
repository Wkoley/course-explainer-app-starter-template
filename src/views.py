from flask import render_template, abort
from models import courses

def index():
    return render_template('index.html')

def course(course_id):
    if course_id < 1 or course_id > len(courses):
        abort(404)
    course = courses[course_id - 1]
    return render_template('course.html', course=course)