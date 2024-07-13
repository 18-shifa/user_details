from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
