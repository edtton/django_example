from django.urls import path 
from . import views 

# define app configuration name 
app_name = 'example_app'

# map views to URL configurations 
urlpatterns = [
    path("index", views.index, name="index"),
    path("greet", views.greet, name="greet")
]