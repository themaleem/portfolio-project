from django.urls import path
from jobs import views
# app_name="jobs"
urlpatterns = [
    path(r'', views.project, name="project"),
    path('<int:job_id>',views.jobdetail,name="jobdetail"),
]
