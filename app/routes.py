#!/usr/bin/python
# -*- coding: <UTF-8> -*-

from app import app
from flask import render_template, redirect, flash, url_for, session
from app.forms import TypeOneForm, ViolationOne, ViolationTwo


@app.route('/')
def index():
    return render_template('index.html', title="Välkommen!")


@app.route('/bestrid', methods=['GET','POST'])
def bestrid():
    form = TypeOneForm()
    if form.validate_on_submit():
        if form.violation.data:
            session['violation'] = form.violation.data
            return redirect(url_for('bestrid01'))
        else:
            return redirect(url_for('index'))
    return render_template('bestrid.html', title="Bestrida", form=form)


@app.route('/test')
def test():
    return render_template('producttest.html')


@app.route('/bestrid01', methods=['GET', 'POST'])
def bestrid01():
    #select from the list of violations.
    violation = session.get('violation')
    if violation == 1:
        form = ViolationOne()
    elif violation == 2:
        form = ViolationTwo()

    #Do stuff with the formdata
    if form.validate_on_submit():
        message = []
        for fieldname, value in form.data.items():
            message.append([fieldname, value])
        flash(message)
        return redirect(url_for('index'))
    return render_template('bestridxx.html', title='Bestrid', form=form)


