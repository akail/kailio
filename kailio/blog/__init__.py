from flask import Blueprint
blog = Blueprint('blog', __name__, url_prefix='/blog')

from kailio.blog import views, errors
