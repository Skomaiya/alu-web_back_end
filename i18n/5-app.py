#!/usr/bin/env python3
"""
A Basic Flask application with user login simulation.
"""
from typing import Dict, Union
from flask import Flask, g, request, render_template
from flask_babel import Babel


class Config:
    """
    Application configuration class.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Babel for localization
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match locale from the request.
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: Union[str, None]) -> Union[Dict[str, Union[str, None]], None]:
    """
    Retrieve user dictionary if ID is valid, otherwise return None.
    """
    try:
        user_id = int(user_id) if user_id else None
        return users.get(user_id)
    except ValueError:
        return None


@app.before_request
def before_request():
    """
    Execute before every request:
    - Retrieve user based on login_as parameter.
    - Store the user object in Flask's global `g` object.
    """
    g.user = get_user(request.args.get('login_as'))


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the main HTML page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
