from django.shortcuts import render
from .models import Job #
# Create your views here.

def home(request):
    #access data from the db call Job model (Job.objects = get all Job objects from DB)
    jobs = Job.objects
    return render(request,'jobs/home.html', {'jobs': jobs}) #list jobs in dictionary to display in jobs.html