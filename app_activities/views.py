from django.shortcuts import render,redirect 
from .forms import ImagePostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Image,Comment,Like


#views functions
@login_required
def home(request): 
  posts=Image.objects.all()

  return render (request,'homepage.html',{"posts": posts})

@login_required
def post_image(request): 
  '''Function for new image post'''
  current_user = request.user
  if request.method == 'POST':
    form = ImagePostForm(request.POST, request.FILES)
    if form.is_valid():
      image_post = form.save(commit=False)
      image_post.user = current_user
      image_post.save()
    messages.success(request,'Image successfully posted')
    return redirect('imagePosts')
  else:
    form = ImagePostForm()
  return render(request, 'posts/new_post.html', {"form": form})

@login_required
def images(request): 
  '''Function to display posted images'''
  posts=Image.objects.all()
  return render(request,'posts/posts.html', {"posts": posts})
  
@login_required 
def comment(request,id):
  current_user = request.user 
  image = Image.objects.filter(id=id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.image = image
      comment.user = current_user
      comment.save()
      
      image.comments = image.comments + 1
      image.save()
      
      comments = Comment.objects.filter(image=image.id).all()
     
      return redirect('/')
  else:
    form = CommentForm()
    comments = Comment.objects.filter(image=image.id).all()
   
  return render(request,'comments.html',{"form":form,'comments':comments,"image":image,"user":current_user})   

@login_required
def like_pic(request, id):
  image = Image.objects.filter(id=id).first()
  likes = Like.objects.filter(post=image).first()

  if Like.objects.filter(post=image, user=request.user).exists():

    likes.delete()

    image = Image.objects.get(id=id)

    if image.likes == 0:
      image.likes = 0
      image.save()
    else:
      image.likes -= 1
      image.save()
    return redirect('/')
  else:
    likes = Like(post=image, user=request.user)
    likes.save()
  
    image = Image.objects.get(id=id)
    image.likes += 1
    image.save()
    return redirect('/')