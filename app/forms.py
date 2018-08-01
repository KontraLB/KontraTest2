from flask_wtf import FlaskForm
from wtforms import StringField, TextField, RadioField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class TypeOneForm(FlaskForm):
    violation = IntegerField("Vilket övertädelsenummer gäller det?", validators=[DataRequired(), NumberRange(min=0, max=100, message="mellan 0 och 100")])
    place = RadioField('Vart fick du bötern?', choices=[('sthlm','Stockholm'),('lnkpg','Linköping')],
                        validators=[DataRequired()])
    submit = SubmitField('Klar')
