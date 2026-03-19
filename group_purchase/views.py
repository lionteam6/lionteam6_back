from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

from .forms import PostForm

def home(request):
  posts = Post.objects.order_by('-created_at')
  return render(request, 'home.html', {'posts': posts})

def detail(request, post_id):
  post_detail=get_object_or_404(Post, pk=post_id)
  return render(request, 'detail.html', {'post': post_detail})

def new(request) :
  form=PostForm()
  return render(request, 'new.html', {'form' : form})

def create(request) :
  form=PostForm(request.POST, request.FILES)
  if form.is_valid():
    new_blog=form.save(commit=False)
    new_blog.save()
    return redirect('group_purchase:detail', new_blog.id)
  return redirect('group_purchase:home')

def delete(request, post_id) :
  delete_blog = get_object_or_404(Post, pk=post_id)
  delete_blog.delete()
  return redirect('group_purchase:home')

def update_page(request, post_id) :
  update_group_purchase = get_object_or_404(Post, pk=post_id)
  return render(request, 'update.html', {'update_group_purchase' : update_group_purchase})

def update_post(request, post_id) :
  update_group_purchase = get_object_or_404(Post, pk=post_id) 
  update_group_purchase.title = request.POST['title']
  update_group_purchase.content = request.POST['content']
  update_group_purchase.item_name = request.POST['item_name']
  update_group_purchase.price = request.POST['price']
  update_group_purchase.max_participants= request.POST['max_participants']
  update_group_purchase.location= request.POST['location']
  update_group_purchase.save()
  return redirect('group_purchase:home')