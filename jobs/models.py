from django.db import models

# Create your models here.

#DB table
class Job(models.Model):
        #upload a image
    image = models.ImageField(upload_to='images/')
        #input summary of job
    summary = models.CharField(max_length=200)
        #input github link
    github = models.URLField(max_length=100, default='') #default is 200


#python manage.py migrate
#run python manage.py check; this checks for any problems in your project without making migrations or touching the database.
#The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables
#according to the database settings in your mysite/settings.py file and the database migrations shipped with the app '''

#Steps to make changes/updates to the DataBase
''' 
1) make changes in this file (models.py)
    - add app to mysite/settings.py (INSTALLED_APPS settings) before doing step 2 
2) run 'python manage.py makemigrations <name_of_app>' to create migrations for those changes 
3) run 'python manage.py migrate' to apply those changes to the db
'''