from blog import views
from django.urls import path
app_name='blog'
urlpatterns = [
    path('', views.home, name="home"),
    path('<int:blog_id>',views.blogdetail,name="detail"),
]
