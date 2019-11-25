#URLConf
from django.urls import path, include

from . import views 
#urlpatterns must be as is (static)
#The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name. 

urlpatterns = [

    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.details, name='detail')
]