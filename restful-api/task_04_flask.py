#!/usr/bin/python3
"""
A simple Flask API to manage user data.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the dictionary from POST data."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
