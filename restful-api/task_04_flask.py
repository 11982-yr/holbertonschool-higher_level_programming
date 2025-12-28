#!/usr/bin/python3
"""
Task 4: Develop a Simple API using Python with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"

@app.route("/status", methods=["GET"])
def status():
    """Status endpoint."""
    return "OK"

@app.route("/data", methods=["GET"])
def data():
    """Return a JSON list of all usernames."""
    return jsonify(list(users.keys()))

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return the full object for a given username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user_obj = {
    "username": username,
    "name": payload.get("name"),
    "age": payload.get("age"),
    "city": payload.get("city")
    }

    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201

if __name__ == "__main__":
    app.run()
