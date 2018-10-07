from flask_wtf import FlaskForm
from wtforms import StringField, TextField, RadioField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class TypeOneForm(FlaskForm):
    violation = IntegerField("Vilket övertädelsenummer gäller det?", validators=[DataRequired(), NumberRange(min=0, max=100, message="mellan 0 och 100")])
    place = RadioField('Vart fick du bötern?', choices=[('sthlm','Stockholm'),('lnkpg','Linköping')],
                        validators=[DataRequired()])
    submit = SubmitField('Nästa')


class Q01(FlaskForm):
    q1 = RadioField('Har du parkerat inom tätbebyggt område som är terräng?', choices=[('yes','ja'),('no','nej')],
                         validators=[DataRequired()])
    q2 = RadioField('Har du parkerat på en cyckelbana eller gångbana?',
                         choices=[('jaCyckelbana', 'ja cyckelbana'), ('jaGångbana', 'Ja gångbana'), ('no', 'nej')],
                         validators=[DataRequired()])
    submit = SubmitField('Nästa')



class Q02(FlaskForm):
    q1 = RadioField('Har du parkerat på en gångbana?',
                     choices=[('yes', 'ja'), ('no', 'nej')])

    q2 = RadioField('Har du parkerat på en cykelbana?',
                    choices=[('yes', 'ja'), ('no', 'nej')])
    submit = SubmitField('Klar')


class Q03(FlaskForm):
    q1 = RadioField('Gjordes parkeringen på en väg? (dvs inte exempelvis på en parkeringsplats',
                    choices=[('yes', 'ja'), ('no', 'nej')])
    q2 = RadioField('Har du parkerat mot färdriktningen, dvs på vänster sida i färdriktningen?',
                    choices=[('2.1.1', 'Ja men det fanns järnvägs- eller spårvagnsspår på högra sidan'),
                             ('2.1.2', 'Ja men gatan var enkelriktad'),
                             ('2.1.3', 'Nej')])
    q3 = RadioField('Fanns ett förbud mot parkering på vänster sida utmärkt med vägskylt?',
                    choices=[('yes','ja'), ('no', 'nej')])
