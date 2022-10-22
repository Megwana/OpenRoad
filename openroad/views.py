"""import blueprint from flask"""
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Roadtrip
from openroad import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/trips')
@login_required
def trips():
    return render_template("trips.html", user=current_user)


@views.route('/preview')
def previewtrips():
    return render_template("preview.html", user=current_user)

@views.route('/plan', methods=['GET', 'POST'])
def plans():
    if request.method == 'POST':
        plan = request.form.get('plan')
        if len(plan) <= 1:
            flash('Note is too short!', category='error')
        else:
            new_plan = Roadtrip(data=plan, user_id=current_user.id)
            db.session.add(new_plan)
            db.session.commit()
            flash('Trip note added!', category='success')

    return render_template("plan.html", user=current_user)
