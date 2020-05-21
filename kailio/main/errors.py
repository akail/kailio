from flask import render_template
from kailio.main import main

@main.app_errorhandler(500)
def internal_server_error(e):
    """
    :param e: Error
    :return: 500 Error page
    """
    return render_template("500.html"), 500
