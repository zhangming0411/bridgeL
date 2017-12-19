# coding:utf-8
import os
from flask import current_app, render_template, flash, send_from_directory, send_file
from . import main
from utils import is_folder, Ofile


@main.route('/', methods=['GET', 'POST'])
def index():
    flash(u'测试下flash')
    return render_template('index.html')


# @main.route('/showfiles', methods=['GET', ])
# def showfiles():
#     file_list = os.listdir(current_app.config['FILE_DIR'])
#     return render_template('showfiles.html', file_list=file_list)

@main.route('/showone', defaults={'name': ''})
@main.route('/showone/<path:name>', methods=['GET', 'POST'])
def showone(name):
    fpath = current_app.config['FILE_DIR']
    full_path = os.path.join(fpath, name)
    if not is_folder(full_path):
        return send_file(full_path)
    file_list = []
    file_names = os.listdir(full_path)
    for f in file_names:
        fo = Ofile(fpath, name, f)
        file_list.append(fo)
    return render_template('showfiles.html', file_list=file_list)


@main.route('/downloads/<filename>')
def downloads(filename):
    return send_from_directory(current_app.config['FILE_DIR'], filename)
