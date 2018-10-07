from flask_wtf import FlaskForm
from wtforms import StringField, TextField, RadioField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class TypeOneForm(FlaskForm):
    violation = IntegerField("Vilket övertädelsenummer gäller det?", validators=[DataRequired(), NumberRange(min=0, max=100, message="mellan 0 och 100")])
    place = RadioField('Vart fick du bötern?', choices=[('sthlm','Stockholm'),('lnkpg','Linköping')],
                        validators=[DataRequired()])
    submit = SubmitField('Klar')

class ViolationOne(FlaskForm):
    q1 = RadioField('Har du parkerat inom tätbebyggt område som är terräng?', choices=[('yes','ja'),('no','nej')],
                         validators=[DataRequired()])
    q2 = RadioField('Har du parkerat på en cyckelbana eller gångbana?',
                         choices=[('jaCyckelbana', 'ja cyckelbana'), ('jaGångbana', 'Ja gångbana'), ('no', 'nej')],
                         validators=[DataRequired()])
    submit = SubmitField('Klar')

class ViolationTwo(FlaskForm):
    q1 = RadioField('Har du stannat eller parkerat inom område där fordon inte får stannas eller parkeras?',
                     choices=[('yes', 'ja'), ('no', 'nej')])
    submit = SubmitField('Klar')