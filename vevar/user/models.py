from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User

# Create your models here.        
class Name(models.Model):
    boy_name=models.CharField(max_length=30)
    girl_name=models.CharField(max_length=33)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(default=date.today)

    class Meta:
        db_table='name'

class Vevar(models.Model):
    vevaname=models.CharField(max_length=50)
    village=models.CharField(max_length=250)
    vevar=models.IntegerField()
    date=models.DateTimeField(default=datetime.today)
    name=models.ForeignKey(Name,on_delete=models.CASCADE)

    class Meta:
        db_table='vevar'

    
    