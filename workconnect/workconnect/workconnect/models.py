from django.db import models

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

    class Meta:
        ordering = ['created']

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