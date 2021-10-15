from django.shortcuts import render

#views functions
def home(request): 
  return render (request,'base.html')