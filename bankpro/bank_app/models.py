from django.db import models

# Create your models here.
class Transcactions(models.Model):
    ttype = models.CharField(max_length=100)
    tamount = models.CharField(max_length=60)
    tmode = models.CharField(max_length=150)

    def __str__(self):
        return self.ttype

class profile(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField(max_length=100)
    image = models.ImageField(upload_to='ProfilePhotos',blank=False)
    nationalality = models.CharField(max_length=200)
    enquired = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name