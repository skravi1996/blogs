from django.urls import path, include

from . import views
from blogapp.views import  BlogView, PublicBlogView


urlpatterns = [
    path('blogs/', BlogView.as_view() , name='blogs'),
    path('publicblogs/', PublicBlogView.as_view(), name='publicblogs'),
    #path('home2',views.home)
  
]



