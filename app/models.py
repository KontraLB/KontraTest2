from app import db

questions = db.Table('questions',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id')),
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.id'))
)

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String(10))
    questions = db.relationship(
        'Question', secondary=questions,
        )


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
