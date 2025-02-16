#!/usr/bin/env python3
"""
Flask app that supports user login simulation with localization.
"""
from flask import Flask, render_template, request, g

app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Retrieve a user dictionary by user ID.
    Returns None if the user ID is not found.
    """
    try:
        return users.get(int(user_id))
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """
    Run before every request.
    Checks if a user is logged in and sets g.user.
    """
    user_id = request.args.get("login_as")
    g.user = get_user(user_id)


@app.route('/')
def index():
    """
    Home page route.
    Displays a welcome message based on user authentication.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
