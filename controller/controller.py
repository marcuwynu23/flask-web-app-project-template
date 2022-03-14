from flask import Flask, render_template, redirect, request, session,abort
from jinja2 import TemplateNotFound


def home_control():
  try:
    session["name"] = "mark Wayne"
    data = {
      'info' : [
      {'#' : 1,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 2,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 3,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 4,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 5,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 6,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 7,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 8,'name' : 'Mark','gender' : 'Male','age' : 23}      
      ]
    }
    return render_template('features/home.html',data=data)
  except TemplateNotFound:
    abort(404)



def contact_control():
  try:
    return render_template('features/contact.html')
  except TemplateNotFound:
    abort(404)



def about_control():
  try:
    return render_template('features/about.html')
  except TemplateNotFound:
    abort(404)