#!/usr/bin/python3
"""
Task 5: API Security and Authentication Techniques
"""

from flask import Flask, jsonify, request
from Flask_HTTPAuth import BasicHTTPAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import (
        JWTManager,
        create_access_token,
        jwt_required(),
        get_jwt_identity()
)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "jwt_super-secret"

auth = BasicHTTPAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", 
              "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", 
               "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password


@app.route("/basic-protected", methods=["GET"])
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    

@app.route("/jwt-protected", methods=["GET"])
def jwt_protected():
    

@app.route("/admin-only", methods=["GET"])
def admin_only():
