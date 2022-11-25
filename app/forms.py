from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, IntegerField, HiddenField
from wtforms.validators import DataRequired, ValidationError, EqualTo

class CreateQuestionForm(FlaskForm):
	precipitation = IntegerField('Annual Precipitation Value(mm)', validators=[DataRequired()])
	temperature = IntegerField('Average Annual Temperature(F)', validators=[DataRequired()])
	methane = IntegerField('Methane (million metric tons of carbon dioxide equivalent)', validators=[DataRequired()])
	nitrous_oxide = IntegerField('Nitrous oxide (million metric tons of carbon dioxide equivalent)', validators=[DataRequired()])
	submit = SubmitField('Submit')





	