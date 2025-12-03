#!/usr/bin/python3
"""
Simple API built with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users database
users = {}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():

    # Parse JSON
    try:
        data = request.get_json()
        if data is None:
            raise ValueError
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # Validate username
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to database
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()

