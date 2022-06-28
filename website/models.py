import math
import pandas as pd
from flask import Blueprint
import os
import glob
from website import ALLOWED_EXTENSIONS

models = Blueprint('models', __name__)
# Square root curve

def square_curve(orig, new_grades):
        for grade in orig:
            new_grade = round(math.sqrt(grade) * 10, 2)
            new_grades.append(new_grade)
        return new_grades


# Determines the amount to add to all scores
def modifier(grade):
    if grade >= 90 and grade <= 100:
        curved_mod = (100 - grade)
    elif grade >= 80 and grade < 90:
        curved_mod = (90 - grade)
    elif grade >= 70 and grade < 80:
        curved_mod = (80 - grade)
    elif grade >= 60 and grade < 70:
        curved_mod = (70 - grade)
    else:
        curved_mod = (60 - grade)
    return curved_mod


# Adds the modifier to the original score
def max_curve(curved_mod, orig, new_grades):
    for grade in orig:
        curved_grade = round(grade + curved_mod, 2)
        new_grades.append(curved_grade)
    return new_grades


# 10 point curve function
def ten_point(orig, new_grades):
    for grade in orig:
        curved_grade = round(grade + 10, 2)
        new_grades.append(curved_grade)
    return new_grades

def delete_downloads(DOWN_PATH):
    try:
        cwd = os.getcwd()
        extension = "csv"
        os.chdir(DOWN_PATH)
        result = glob.glob('*.{}'.format(extension))
        for file in result:
            os.remove(file)
        os.chdir(cwd)
        return "success"
    except FileNotFoundError as error:
        return "error"

def delete_uploads(UP_PATH):
    try:
        cwd = os.getcwd()
        extension = "csv"
        os.chdir(UP_PATH)
        result = glob.glob('*.{}'.format(extension))
        for file in result:
            os.remove(file)
        os.chdir(cwd)
        return "success"
    except FileNotFoundError:
        return "error"

