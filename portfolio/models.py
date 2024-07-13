from django.db import models
from django.contrib.auth.models import User

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)
    field_of_study = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.degree

class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    issuing_organization = models.CharField(max_length=250)
    description = models.TextField()
    issue_date = models.DateField()

    def __str__(self):
        return self.title
