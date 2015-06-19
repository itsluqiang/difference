from flask import jsonify, request, g, abort, url_for, current_app
from datetime import datetime
from ..main.calc_diff import get_diff
from .. import db
from ..models import Queries
from . import api
from .errors import bad_request

@api.route('/difference')
def get_n_diff():
	n = request.args.get('number', type=int)
	if not isinstance(n, int) or n < 1 or n > 100:
		return bad_request("Number should be an integer between 1 and 100!")

	# Check whether n has been queried before
	nHistory = Queries.get_number_history(n)

	# Calulate difference(if needed). Insert new query to database
	qDateTime = datetime.utcnow()
	qValue = nHistory['value'] if nHistory['occurrences'] != 0 else get_diff(n)
	newQuery = Queries(timestamp = qDateTime, number = n, value = qValue)
	db.session.add(newQuery)

	# Return api result
	return jsonify({
		'datetime':str(qDateTime.strftime('%Y-%m-%d %H:%M:%S')),
		'value': qValue,
		'number': n,
		'occurrences':nHistory['occurrences'] + 1
	})

