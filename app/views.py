from flask import render_template, request, redirect, url_for
from .models import Data
from flask import current_app as app

@app.route('/')
def index():
    return redirect(url_for('events'))

@app.route('/events/')
def events():
    page = request.args.get('page', 1, type=int)
    pagination = Data.query.paginate(page, per_page=20)
    return render_template('events_list.html', pagination=pagination)

@app.route('/event/<string:event_id>/')
def event_detail(event_id):
    data = Data.query.get_or_404(event_id)
    return render_template('event_detail.html', data=data, resp=data.response)
