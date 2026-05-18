from flask import Blueprint, render_template, redirect, request, flash, jsonify
from server.index import createStudent, deleteStudentById, getAll, getById, updateStudent
from flask_jwt_extended import jwt_required

students_bp = Blueprint("students", __name__)


@students_bp.route("/")
def home():
    students = getAll()
    return render_template("index.html", students=students)

@students_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]
        createStudent(name, email, age)
        flash("Student created successfully! ✅")
        return redirect("/")
    return render_template("create.html")



@students_bp.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        print("ID===", id)
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]
        updateStudent(id, name, email, age)
        flash("Student updated successfully! ✅")
        return redirect("/")
    student = getById(id)
    return render_template("update.html", student=student)

@students_bp.route("/delete/<id>", methods=["GET"])
def delete(id):
    deleteStudentById(id)
    flash("Student deleted successfully! ✅")
    return redirect("/")


# GET /api/students — get all students
@students_bp.route("/students", methods=["GET"])
@jwt_required()
def get_all():
    students = getAll()
    return jsonify(students), 200


@students_bp.route("/students/<id>", methods=["GET"])
@jwt_required()
def get_by_id(id):
    student = getById(id)
    return jsonify(student), 200

@students_bp.route("/students", methods=["POST"])
@jwt_required()
def create_student():
    name = request.json["name"]
    email = request.json["email"]
    age = request.json["age"]
    if name == "" or email == "" or age == "":
        return jsonify(message="Invalid requests"), 404
    
    createStudent(name, email, age)
    return jsonify(message="Success"), 201

@students_bp.route("/students/<id>", methods=["PUT"])
@jwt_required()
def update_student(id):
    name = request.json["name"]
    email = request.json["email"]
    age = request.json["age"]
    if name == "" or email == "" or age == "":
        return jsonify(message="Invalid requests"), 400
    
    s = getById(id)
    if not s:
        return jsonify(message="Student not found"), 404
    updateStudent(id, name, email, age)
    return jsonify(message="Success"), 200


@students_bp.route("/students/<id>", methods=["DELETE"])
@jwt_required()
def delete_student(id):
    s = getById(id)
    if not s:
        return jsonify(message="Student not found"), 404
    deleteStudentById(id)
    return jsonify(message="Success"), 200