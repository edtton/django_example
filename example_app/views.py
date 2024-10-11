from django.shortcuts import render

# import Django HttpResponse library 
from django.http import HttpResponse 

# import Django forms library 
from django import forms 

# import Django redirect library
from django.shortcuts import redirect

from django.db import models
from .models import Students

# define our Form class 
class NewForm(forms.Form):
    name = forms.CharField(label="Enter Name")

# define a "view" 
def index(request): 
    return render(request, "example_app/index.html", {'form':NewForm()})

def greet(request): 
    if request.method == 'POST': 
        form = NewForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data['name']
            student = Students.objects.create(name=name)
            return render(request, "example_app/greet.html", {'students':Students.objects.all()})

    return redirect(index)
