#!/usr/bin/python
# -*- coding: <UTF-8> -*-

from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import TypeOneForm, ViolationOne, ViolationTwo

@app.route('/')
def index():
    return render_template('index.html', title="Välkommen!")

@app.route('/bestrid', methods=['GET','POST'])
def bestrid():
    form = TypeOneForm()
    if form.validate_on_submit():
        if form.violation.data == 1:
            return redirect(url_for('bestrid01'))
        elif form.violation.data == 2:
            return redirect(url_for('bestrid02'))
        else:
            return redirect(url_for('index'))
    return render_template('bestrid.html', title="Bestrida", form=form)


@app.route('/test')
def test():
    return render_template('producttest.html')


@app.route('/bestrid01', methods=['GET', 'POST'])
def bestrid01():
    form = ViolationOne()
    return render_template('bestridxx.html', title='Bestrid', form=form)


@app.route('/bestrid02', methods=['GET', 'POST'])
def bestrid02():
    form = ViolationTwo()
    return render_template('bestridxx.html', title='Bestrid', form=form)

