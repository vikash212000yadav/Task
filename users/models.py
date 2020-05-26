from django.db import models

# Create your models here.


class User(models.Model):
    id = models.SlugField(primary_key=True, max_length=200)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=100)

    def __str__(self):
        return self.real_name


class Activity(models.Model):
    start_time = models.DateTimeField(default="2020-02-01 01:34:45")
    end_time = models.DateTimeField(default="2020-02-01 02:34:45")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
