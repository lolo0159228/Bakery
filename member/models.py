from django.db import models
from django.utils import timezone

# Create your models here.

class MemberType(models.Model):
    user_type = models.CharField(default='N',max_length=1)

    def __str__(self):
        return self.user_type


class Member(models.Model):
    accountID = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=20,blank=False)
    username = models.CharField(max_length=10)
    email = models.EmailField(blank=False)
    type = models.ForeignKey(to=MemberType,on_delete=models.CASCADE)
    createdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.accountID

