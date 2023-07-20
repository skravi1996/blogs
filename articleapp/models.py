from django.db import models
from blogapp.models import Blog2

# Create your models here.

class Article(models.Model):
    title = models.ForeignKey(Blog2,on_delete=models.CASCADE)
    phone=models.CharField('Phone',blank=True, max_length=15)
    address1=models.CharField('Address',max_length=150, blank=False,null=True)
    text = models.TextField()

    def __str__(self):
        return self.title.title_1
    
class Info(models.Model):
    phone = models.ForeignKey(Article,on_delete=models.CASCADE)
    address1=models.CharField('Address',max_length=150, blank=False,null=True)
    text = models.TextField()

    def __str__(self):
        return self.phone.phone