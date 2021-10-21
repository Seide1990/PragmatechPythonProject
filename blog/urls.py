
from django.urls import path
from .views import (index,
   about,
   blog_list,
   blog_detail
)
app_name='blog'
urlpatterns = [
 
    path('blog-detail/<int:id>/',blog_detail,name='blog-detail'),
    path('index/',index,name='index'),
    path('about/',about,name='about'),
  

    
]
