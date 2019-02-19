from django.shortcuts import render
from jobs.models import Jobs
# Create your views here.
def home(request):
    return render(request, 'jobs/home.html')

def project(request):
    jobs = Jobs.objects.all()
    context = {
        'jobs': jobs
    }
    return render(request,'jobs/project.html',context)