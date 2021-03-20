from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class tvwatched(models.Model):
    tvid=models.IntegerField()
    watchers=models.ForeignKey(User,on_delete=models.CASCADE)
    #rate=models.IntegerField()

class tvwatching(models.Model):
    tvid=models.IntegerField()
    watchers=models.ForeignKey(User,on_delete=models.CASCADE)
    #rate=models.IntegerField()

