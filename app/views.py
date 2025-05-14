from flask import Blueprint, render_template, request, redirect, url_for
from .models import Data

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return redirect(url_for('main.events'))

@bp.route('/events/')
def events():
    # get the severity == low/medium/high
    severity = request.args.get('severity', type=str)
    page = request.args.get('page', 1, type=int)

    # basic searching
    query = Data.query
    if severity:
        query = query.filter_by(attack_severity=severity.capitalize())

    # into pages
    pagination = query.paginate(page, per_page=20)

    return render_template(
        'events_list.html',
        pagination=pagination,
        current_severity=severity  # Template return for activating
    )
    
@bp.route('/event/<string:event_id>/')
def event_detail(event_id):
    data = Data.query.get_or_404(event_id)
    return render_template('event_detail.html', data=data, resp=data.response)
