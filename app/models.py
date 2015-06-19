from . import db
from sqlalchemy import func
from . import moment
from datetime import datetime

class Queries(db.Model):
	__tablename__ = 'queries'
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	value = db.Column(db.Integer)
	number = db.Column(db.Integer)

	def __repr__(self):
		return '<%s %s %s>' % (str(self.timestamp.strftime('%Y-%m-%d %H:%M:%S')), str(self.value), str(self.number),)

	@staticmethod
	def get_number_history(n):
		ds = db.session.query(func.count(), Queries.value).filter(Queries.number == n).first()
		result = {'occurrences':ds[0], 'value':ds[1]}
		return result


