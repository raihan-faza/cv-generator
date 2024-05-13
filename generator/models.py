from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=200, default=None)
    github = models.CharField(max_length=200, default=None)
    description = models.TextField(max_length=100)


class Project(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    github_link = models.CharField(max_length=500, default=None)


class Degree(models.Model):
    institution_name = models.CharField(max_length=100)
    enter = models.DateField()
    graduate = models.DateField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
