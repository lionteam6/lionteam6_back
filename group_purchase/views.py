from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, User

from .forms import PostForm

def home(request):
  posts = Post.objects.order_by('-created_at')
  user = User.objects.first()

  return render(request, 'home.html', {'posts': posts, 'user_id' : user.id,})

def detail(request, post_id, user_id):
  post_detail=get_object_or_404(Post, pk=post_id)
  current_user = get_object_or_404(User, pk=user_id)

  is_participant = post_detail.participants.filter(pk=current_user.pk).exists()
  is_author = post_detail.user.pk == current_user.pk


  return render(request, 'detail.html', {'post': post_detail, 'current_user': current_user, 'is_participant': is_participant, 'is_author': is_author,})

def new(request, user_id) : #빈 작성 폼 보여주는 함수 (URL에서 user_id 받아서 html로 넘김)
  form=PostForm()
  return render(request, 'new.html', {'form' : form, 'user_id' : user_id})

def create(request, user_id) : 
  user = get_object_or_404(User, pk = user_id)

  if request.method == 'POST':
    form=PostForm(request.POST, request.FILES)
    if form.is_valid():
      new_post=form.save(commit=False)
      new_post.user = user
      new_post.save()
      return redirect('group_purchase:detail', new_post.id , user.id)
    return redirect('group_purchase:home')

def delete(request, post_id) :
  delete_post = get_object_or_404(Post, pk=post_id)
  delete_post.delete()
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

def join_post(request, post_id, user_id): #참여하기 함수
    post = get_object_or_404(Post, pk=post_id)
    current_user = get_object_or_404(User, pk=user_id)

    # 작성자는 자기 글에 참여하지 못하게 하고 싶다면
    if post.user != current_user:
        # 이미 참여 중인지 확인
        if not post.participants.filter(pk=current_user.pk).exists():
            # 모집 인원 초과 방지
            if post.participants.count() < post.max_participants:
                post.participants.add(current_user)

    return redirect('group_purchase:detail', post.id, current_user.id)

def leave_post(request, post_id, user_id): #참여 취소 함수
    post = get_object_or_404(Post, pk=post_id)
    current_user = get_object_or_404(User, pk=user_id)

    if post.participants.filter(pk=current_user.pk).exists():
        post.participants.remove(current_user)

    return redirect('group_purchase:detail', post.id, current_user.id)