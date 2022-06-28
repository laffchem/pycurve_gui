from flask import Blueprint, Response, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename, send_file
import pandas as pd
import math
from .curves import square_curve, modifier, max_curve, ten_point

import os

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    # Gets info from form and saves file to upload folder
    if request.method == "POST":
        file = request.files['file']
        file.save(os.path.join("uploads", secure_filename(file.filename)))
        column_name = request.form.get('curved-col')
        curve_option = request.form.get('curve-apply')
        curved_file = f"{request.form.get('curved-file')}.csv"
        # Get the Data Frame
        new_grades = []
        grades = pd.read_csv(os.path.join("uploads", file.filename))
        orig = grades[column_name]
        highest = max(orig)
        if curve_option == "1":
            square_curve(orig=orig, new_grades=new_grades)
        elif curve_option == "2":
            curved_mod = modifier(highest)
            max_curve(curved_mod, orig, new_grades)
        elif curve_option == "3":
            ten_point(orig=orig, new_grades=new_grades)
        
        grades['curved'] = new_grades
        grades.to_csv(os.path.join("downloads", curved_file))
        # Deletes the original file from the server to save space
        # and to follow client privacy.
        os.remove(os.path.join("uploads", file.filename))
        return render_template('home.html', curved_file=curved_file)
    return render_template('home.html')


@views.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == "POST":
        curved_file = request.form.get('curved-dl')
        path = os.path.join("downloads", curved_file)
        return send_file(path, as_attachment=True), render_template('download.html')

    return render_template('download.html')