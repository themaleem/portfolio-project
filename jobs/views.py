from django.shortcuts import render
from jobs.models import Jobs
from jobs.forms import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    form = ContactForm(request.POST)
    
    context = {
        'form':form
    }
    if form.is_valid():
        subject = "MESSAGE FROM VISITOR ON MALEEMNG"
        message = form.cleaned_data['message'] + form.cleaned_data['email']
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        # send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
        response = 'Message Sent! I\'ll get back to you soon'
        context = {'response': response, 'form': form}
        


    return render(request, 'jobs/home.html',context)

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
    return render(request, 'jobs/details.html', context)
    
