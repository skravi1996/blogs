from django.contrib import admin
from . import models
from .models import Blog2,Blog

# Register your models here.

admin.site.register(Blog2)
admin.site.register(Blog)
