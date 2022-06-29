from flask import Blueprint, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import pandas as pd
from .models import delete_uploads, square_curve, modifier, max_curve, ten_point, delete_downloads, delete_uploads

import os

UP_PATH = "website/static/uploads"
DOWN_PATH = "website/static/downloads"
ALLOWED_EXTENSIONS = {'csv'}

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    cwd = os.getcwd()
    # should remove files that are in downloads and uploads folder
    delete_downloads(DOWN_PATH)  
    delete_uploads(UP_PATH)
    flash("Previous files deleted", category="success")
    # Gets info from form and saves file to upload folder

    if request.method == "POST":

        file = request.files['file']
        # print(file.filename)
        if file.filename == "":
            flash(message="No selected file", category="error")
            return redirect(request.url)
        if file.filename.rsplit('.', 1)[1].lower()=='csv':
            filename = secure_filename(file.filename)
            file.save(os.path.join(UP_PATH, filename))
        else:
            flash(message="Incorrect file type.", category="error")
            return redirect(request.url)
            

        column_name = request.form.get('curved-col')
        curve_option = request.form.get('curve-apply')
        curved_file = f"{request.form.get('curved-file')}.csv"
        if column_name == "" or curve_option == "Choose the curve you want to apply." or curved_file == ".csv":
            flash(message="Ensure all fields are filled out", category="error")

        # Get the Data Frame
        grades = pd.read_csv(os.path.join(UP_PATH, file.filename))
        # print(grades)
        new_grades = []
        if column_name in grades.columns:
            orig = grades[column_name]
            highest = max(orig)
        else:
            flash(message=f"There is no column named {column_name}", category="error")
            return redirect(request.url)
        # Curved Options
        try:
            if curve_option == "1":
                square_curve(orig=orig, new_grades=new_grades)
            elif curve_option == "2":
                curved_mod = modifier(highest)
                max_curve(curved_mod, orig, new_grades)
            elif curve_option == "3":
                ten_point(orig=orig, new_grades=new_grades)
            else:
                raise KeyError("Must select an option")
        except KeyError:
            flash(message="You must select an option to curve", category="error")
        else:
            grades['curved'] = new_grades
            grades.to_csv(os.path.join(DOWN_PATH, curved_file))
            # Deletes the original file from the server to save space
            # and to follow client privacy.
            delete_uploads(UP_PATH)
            os.chdir(cwd)
        return render_template('download.html', curved_file=curved_file)
    return render_template('home.html')


@views.route('/download', methods=['GET', 'POST'])
def download():
    return render_template('download.html')


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS