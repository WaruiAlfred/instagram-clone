from django.shortcuts import render,redirect
from . forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_activities.models import Image,Follow
from .email import send_welcome_email
from .models import Profile
from django.contrib.auth.models import User

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

def search_results(request):
  
  if 'username' in request.GET and request.GET["username"]:
    search_term = request.GET.get("username")
    found_user = User.objects.filter(username=search_term).first()
    message = f"{search_term}"
    
    current_user = search_term
    logged_in_user = request.user.username
    user_followers = len(Follow.objects.filter(user=current_user))
    user_following = len(Follow.objects.filter(follower=current_user))
    user_followers_list = Follow.objects.filter(user=current_user)
    
    user_followers_data = []
    for i in user_followers_list: 
      user_follower0 = i.follower
      user_followers_data.append(user_follower0)
      
    if logged_in_user in user_followers_data: 
      follow_button_value = 'unfollow'
    else: 
      follow_button_value = 'follow'
      
    posts=Image.objects.all()
  
    context = {
      "posts": posts,
      "current_user":current_user,
      "user_followers":user_followers,
      "user_following":user_following,
      "follow_button_value":follow_button_value,
      "message":message,
      "users": found_user
    }
    
    return render(request, 'search.html',context)

  else:
    message = "That user doesn't exist"
    return render(request, 'search.html',{"message":message})
  
def follow(request): 
  if request.method == 'POST': 
    value = request.POST['value']
    user = request.POST['user']
    follower = request.POST['follower']
    if value == 'follow': 
      followers_count = Follow.objects.create(follower = follower, user = user)
      followers_count.save()
    else:
      followers_count = Follow.objects.get(follower = follower, user = user)
      followers_count.delete()
    return redirect('search_results')