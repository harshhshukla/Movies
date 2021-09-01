from django.db import models
from django.utils import timezone
# Create your models here.

class course(models.Model):
    
    course_id = models.AutoField
    name =  models.CharField(max_length=50)
    desc =  models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to="course\images",default="")
    pub_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name