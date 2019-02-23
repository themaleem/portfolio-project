from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Blogs'
    def summary(self):
        return self.body[1:100]
