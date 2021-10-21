
from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
#from index.views import Home
from blog import views
import blog
#from product import views
from product.views import (product_list,)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('blogs/',views.blog_list,name='blog'),
    path('about/',views.about,name='about'),
    path('product/',product_list,name='product'),
    
]
