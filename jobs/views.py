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
def jobdetail(request, job_id):
    job = Jobs.objects.get(id=job_id)
    context = {
        'job': job
    }
    return render(request,'jobs/details.html',context)