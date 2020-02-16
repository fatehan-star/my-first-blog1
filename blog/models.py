from django.db import models
from django.utils import timezone
from dateutil import relativedelta
from datetime import datetime
# Create your models here.
class Post(models.Model):
    auther = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    day = models.CharField(max_length=20)
    ddate = models.DateField(default=timezone.now)
    intime = models.DateTimeField(default=timezone.now)
    outtime = models.DateTimeField(blank=True, null=True)
    sumtime =  models.CharField(max_length=200)

    def publish(self):
        self.outtime = timezone.now()
        self.save()

    def __str__(self):
        return self.day

class garanty(models.Model):
      author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
      serial = models.CharField(max_length=200)
      start = models.DateTimeField(default=timezone.now)
      stop = models.DateTimeField(blank=True, null=True)
      centername = models.CharField(max_length=2000)
      name_of_model = models.CharField(max_length=200,null=True)

      def __str__(self):
          return self.serial      
       



