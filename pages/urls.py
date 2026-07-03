from django.urls import path 
from . import views 
 


urlpatterns = [
   path('', views.base, name='base'),
   path('major', views.major, name='major'),
   path('masar', views.masar, name='masar'),
   path('blog', views.blog, name='blog'),
]