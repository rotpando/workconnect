from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    lastName = models.CharField(max_length = 100)
    firstName = models.CharField(max_length = 100)
    companyName = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    kvk = models.CharField(max_length = 100)
    jobCategory = models.CharField(max_length = 100)
    userType = models.CharField(max_length = 100)
    premium = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(blank=True, null=True)

class Adver(models.Model):
    title = models.CharField(max_length = 100)
    companyName = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    journey = models.CharField(max_length = 100)
    modality = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    subCategories = models.CharField(max_length = 100, default='None')
    salary = models.IntegerField()
    salaryMin = models.IntegerField()
    salaryMax = models.IntegerField()
    salaryFreq = models.IntegerField()
    description = models.CharField(max_length = 100)
    requirement = models.CharField(max_length = 100)
    zip = models.CharField(max_length = 100)
    authorId = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Prueba(models.Model):
    authorId = models.CharField(max_length = 100)