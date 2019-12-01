from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    modified_on=models.DateField()

    def __str__(self):
        return str(self.user)


class DateModel(models.Model):
    startdate = models.DateField()
    enddate = models.DateField()



