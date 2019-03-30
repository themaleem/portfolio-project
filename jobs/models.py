from django.db import models

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)
    medium_link = models.CharField(max_length=100,blank=True)
    status= models.CharField(max_length=100,blank=True)
    github_link = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Jobs'
        