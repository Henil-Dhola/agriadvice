from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15,unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
class Crops(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
class Requirements(models.Model):
    crop = models.ForeignKey(Crops,on_delete=models.CASCADE,to_field='name')
    soil = models.TextField()
    ph =models.TextField()
    fertility =models.TextField()
    temperature = models.CharField(max_length=255)
    sunlight =models.CharField(max_length=255)
    water = models.CharField(max_length=255)
    fertilizers = models.TextField()
    duration = models.TextField()

    def __str__(self):
        return f"Requirements for {self.crop.name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=200)
    overview = models.TextField()  
    key_features = models.TextField() 
    # image = models.ImageField(upload_to='images/', default='images/background.jpeg', null=True, blank=True)   

    def __str__(self):
        return self.name
    def get_key_features_as_list(self):
        """Returns key features as a list to easily display in template"""
        return self.key_features.split(',')
