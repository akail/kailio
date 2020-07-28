from flask import render_template
from kailio.crm import crm

@crm.app_errorhandler(500)
def internal_server_error(e):
    """
    :param e: Error
    :return: 500 Error page
    """
    return render_template("500.html"), 500
