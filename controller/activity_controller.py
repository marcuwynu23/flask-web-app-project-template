from flask import render_template

class ActivityController():
    def list_activities(self):
        return render_template('features/activity/index.html',context={
            'users': []
        })
    def render_new_activity_page(self):
        return render_template('features/activity/new.html',context={})
    def post_new_activity():
        pass
    def render_update_activity_page(self,id):
        return render_template('features/activity/update.html',context={
          'user': []
        })
    def post_update_activity(self,id):
        pass
    def render_activity(self,id):
        return render_template('features/activity/show.html',context={
          'user': []
        })
    def delete_activity(self,id):
        pass