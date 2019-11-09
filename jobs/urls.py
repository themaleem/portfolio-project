from django.urls import path
from jobs import views
# app_name="jobs"
urlpatterns = [
    path('', views.project, name="project"),
    path('<int:job_pk>',views.jobdetail,name="jobdetail"),
]
