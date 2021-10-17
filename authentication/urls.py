from django.urls import path
from . import views

urlpatterns = [
  path('register/',views.register, name='register'),
  path('profile/',views.profile,name='profile'),
  path('search_user/',views.search_results,name='search_results'),
  path('follow/',views.follow,name='follow'),
]
