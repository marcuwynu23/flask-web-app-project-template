from flask import Flask, render_template, request, redirect, url_for,Blueprint

from controller.activity_controller import ActivityController
activity = Blueprint('activity',__name__)
activity_controller = ActivityController()

@activity.route('/')
def index():
	return activity_controller.list_activities()

@activity.route('/new',methods=['GET','POST'])
def new():
	if request.method == 'POST':
		return activity_controller.post_new_activity()
	else:
		return activity_controller.render_new_activity_page()
    

@activity.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
	if request.method == 'POST':
		return activity_controller.post_update_activity(id)
	else:
		return activity_controller.render_update_activity_page(id)


@activity.route('/show/<int:id>')
def show(id):
	return activity_controller.render_activity(id)


@activity.route('/delete/<int:id>')
def delete(id):
	return activity_controller.delete_activity(id)



