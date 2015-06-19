from flask.ext.wtf import Form
from wtforms import IntegerField, SubmitField
from wtforms.validators import Required, NumberRange


class QueryForm(Form):
    number = IntegerField('Please input the number you want to query:', validators=[Required(), NumberRange(min=1, max=100)])
    submit = SubmitField('Submit')

