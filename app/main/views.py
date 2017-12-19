# coding:utf-8
import os
from flask import current_app, render_template, flash, send_from_directory
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    flash(u'测试下flash')
    return render_template('index.html')


@main.route('/showfiles', methods=['GET', 'POST'])
def showfiles():
    file_list = os.listdir(current_app.config['FILE_DIR'])
    return render_template('showfiles.html', file_list=file_list)


@main.route('/downloads/<filename>')
def downloads(filename):
    return send_from_directory(current_app.config['FILE_DIR'], filename)