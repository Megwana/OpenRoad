"""import blueprint from flask"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)