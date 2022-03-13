from flask import render_template

def home_control():
  try:
    return render_template('features/home.html')
  except TemplateNotFound:
    abort(404)

def about_control():
  try:
    return render_template('features/about.html')
  except TemplateNotFound:
    abort(404)