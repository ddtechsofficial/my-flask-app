from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.auth import createUser, getUserByUserName

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    username = request.json["username"]
    password = request.json["password"]

    existing = getUserByUserName(username)
    if existing:
        return jsonify(message="User already exisit"), 400
    
    createUser(username, password)
    return jsonify(message="Sucessfully registered"), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]

    user = getUserByUserName(username)

    if not user:
        return jsonify(message="User not found"), 404
    
    if user[2] != password:
        return jsonify(message="Invalid credentials"), 401

    token = create_access_token(identity=username)
    return jsonify(message="Login Success", token=token), 200