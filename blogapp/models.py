from django.db import models
import uuid
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


  
# The Blog class inherits from the BaseModel class, and has a one-to-many relationship with the User class      
class Blog(models.Model):
    user =  models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    title_2 = models.CharField(max_length=200)
    blog_text_2= models.TextField()  
    #main_image = models.FileField()   
        
    def __str__(self):
        return self.title_2


class Blog2(models.Model):
    title_1 = models.CharField(max_length=200)
    blog_text= models.TextField()  
    main_image = models.FileField()
    date_1 = models.DateTimeField(auto_now_add=True,editable=False, null=True)
        
    def __str__(self):
        return self.title_1