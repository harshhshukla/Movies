from django.db import models
from django.utils import timezone
# Create your models here.

class favmovie(models.Model):
    favmovie_id = models.AutoField
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    directorName = models.CharField(max_length=50,default="")
    releaseDate = models.DateField(default=timezone.now)
    ratingImdb = models.IntegerField(default=0)
    posters = models.ImageField(upload_to="urfavmovie\images",default="")
    
    def __str__(self):
        return self.name
    
    

class Contact(models.Model):
    favmovie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    PhoneNo = models.IntegerField()
    Email = models.CharField(max_length=50,default="")
    Descriptionn = models.CharField(max_length=50,default="")
    pub_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name
    
    