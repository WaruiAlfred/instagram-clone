from django.urls import path
from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='app_home'),
    path('new_post/',views.post_image,name='new_image_post'),
    path('posts/',views.images,name='imagePosts'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('like/<int:id>/', views.like_pic, name='likeImage'),
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)