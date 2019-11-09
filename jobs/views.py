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
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        messages.success(request,'I got your invitiation to coffee 😊')
        return redirect('home')
    context={
        'home':True
    }

    return render(request, 'jobs/home.html',context)

def project(request):
    jobs = Jobs.objects.all()
    jobs=jobs.order_by('-pk')
    context = {
        'jobs': jobs,
        'projects':True,
    }
    return render(request,'jobs/project.html',context)
def jobdetail(request, job_pk):
    job = Jobs.objects.get(pk=job_pk)
    context = {
        'job': job,
        'details':True
    }
    return render(request, 'jobs/details.html', context)