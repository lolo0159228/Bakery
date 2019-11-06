from django.db import models
from member.models import Member

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(to=Member,on_delete=models.CASCADE)
    productID = models.CharField(max_length=10)
    qty = models.IntegerField()

    def __str__(self):
        return str(self.user) +'__Product :'+(self.productID)

