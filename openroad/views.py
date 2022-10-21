"""import blueprint from flask"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/trips')
@login_required
def trips():
    return render_template("trips.html", user=current_user)

@views.route('/preview')
def sampletrips():
    return render_template("preview.html", user=current_user)