from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import TypeOneForm

@app.route('/')
def index():
    return render_template('index.html', title="Välkommen!")

@app.route('/bestrid', methods=['GET','POST'])
def bestrid():
    form = TypeOneForm()
    if form.validate_on_submit():
        flash('Stad:{} ,Övertädelsenummer:{}'.format(
            form.place.data, form.violation.data))
        return redirect(url_for('index'))
    return render_template('bestrid.html', title="Bestrida", form=form)
