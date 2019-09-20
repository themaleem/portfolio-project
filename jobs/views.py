from django.shortcuts import render,redirect
from jobs.models import Jobs
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=="POST":
        subject = "MESSAGE FROM VISITOR ON MALEEMNG"
        message = request.POST['message'] + request.POST['email']
        emailFrom = request.POST['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
        # messages.success(request,'I got your invitiation to coffee 😊')
        print(subject,emailFrom)
        return redirect('home')

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
    return render(request, 'jobs/details.html', context)

