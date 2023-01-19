from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    lastName = models.TextField()
    firstName = models.TextField()
    companyName = models.TextField()
    password = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    city = models.TextField()
    kvk = models.TextField()
    jobCategory = models.TextField()
    userType = models.TextField()
    premium = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

class Adver(models.Model):
    title = models.TextField()
    companyName = models.TextField()
    city = models.TextField()
    journey = models.TextField()
    modality = models.TextField()
    category = models.TextField()
    sub_categories = models.TextField()
    salary = models.IntegerField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    salary_freq = models.IntegerField()
    description = models.TextField()
    requirement = models.TextField()
    zip = models.TextField()
    authorId = models.TextField()
    location = models.TextField()
