from django.db import models

# Create your models here.
class userdata(models.Model):
    id = models.AutoField
    name = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, max_length=300)
    mobile = models.CharField(unique=True, max_length=10)
    password = models.CharField(max_length=500)
    image = models.ImageField(null=True)
    unique_key = models.CharField(max_length=6,unique=True,default=0)

    def __str__(self):
        return self.name
        
class Verification_otp(models.Model):
    id = models.AutoField
    otp = models.CharField(max_length=4)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.otp
    

class logs(models.Model):
    id = models.AutoField
    operation = models.CharField(max_length=1000)
    data = models.CharField(max_length=1000)
    time = models.DateTimeField()

    def __str__(self):
        return self.data
    