from django.shortcuts import render,redirect
from . forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_activities.models import Image
from .email import send_welcome_email

#register view function
def register(request): 
  if request.method == 'POST': 
    form  =UserRegistrationForm(request.POST)
    if form.is_valid(): 
      form.save()
      name = form.cleaned_data.get('username')
      email = form.cleaned_data.get('email')
      send_welcome_email(name,email)
      
      messages.success(request,f'Your account has been created!You can now login.')
      return redirect('login')
  else:
    form  =UserRegistrationForm()
  return render(request,'authentication/register.html',{"form":form})

#profile view function
@login_required
def profile(request): 
  posts =   Image.objects.filter(user=request.user).all()
  print(f'Found posts {posts}')
  if request.method == 'POST': 
    u_form = UserUpdateForm(request.POST,instance=request.user)
    p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid(): 
      u_form.save() 
      p_form.save()
      messages.success(request,f'Your account has been updated.')
      return redirect('profile')
  else: 
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
  
  context = {
    'posts':posts,
    'u_form':u_form,
    'p_form':p_form,
  }
  return render(request,'authentication/profile.html',context)
