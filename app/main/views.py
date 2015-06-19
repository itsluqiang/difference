from flask import render_template, url_for, request, session, redirect
from .. import db
from . import main
from .forms import QueryForm
from ..models import Queries

@main.route('/', methods = ['GET', 'POST'])
def index():
	form = QueryForm()
	ds = []
	session.pop('number', None)
	if form.validate_on_submit():
		session['number'] = form.number.data
		form.number.data = ''
		ds = Queries.query.filter(Queries.number == session['number']).order_by(Queries.timestamp.desc()).all()
	return render_template('index.html', form = form, number = session.get('number'), ds = ds)
