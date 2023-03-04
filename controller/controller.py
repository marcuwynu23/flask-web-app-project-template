from flask import Flask, make_response, render_template, redirect, request, session,abort,make_response
from jinja2 import TemplateNotFound


def home_control():
  res,req = make_response,request
  try:
    session["name"] = "marco"
    context = {
      'info' : [
      {'#' : 1,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 2,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 3,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 4,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 5,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 6,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 7,'name' : 'Mark','gender' : 'Male','age' : 23},
      {'#' : 8,'name' : 'Wayne','gender' : 'Male','age' : 23}      
      ]
    }
   
    return render_template('features/home.html',context=context)
  except TemplateNotFound:
    abort(404)



def contact_control():
  res,req = make_response,request
  print(session['name'])
  try:
    return render_template('features/contact.html',context={})
  except TemplateNotFound:
    abort(404)



def about_control():
  res,req = make_response,request
  try:
    return render_template('features/about.html',context={})
  except TemplateNotFound:
    abort(404)