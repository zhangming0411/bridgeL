# coding:utf-8
from flask import render_template, flash
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

