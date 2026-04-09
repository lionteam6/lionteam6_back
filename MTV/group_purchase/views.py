from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

from .forms import PostForm

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)

    is_participant = False
    is_author = False

    if request.user.is_authenticated:
        is_participant = post_detail.participants.filter(pk=request.user.pk).exists()
        is_author = (post_detail.user.pk == request.user.pk)

    return render(request, 'detail.html', {
        'post': post_detail,
        'is_participant': is_participant,
        'is_author': is_author,
    })

def new(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    form = PostForm()
    return render(request, 'new.html', {'form': form})

def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('group_purchase:detail', new_post.id)

        print(form.errors)
        return render(request, 'new.html', {'form': form})

    return redirect('group_purchase:home')

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if post.user != request.user:
        return redirect('group_purchase:home')

    post.delete()
    return redirect('group_purchase:home')


def update_page(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if post.user != request.user:
        return redirect('group_purchase:home')

    return render(request, 'update.html', {'update_group_purchase': post})


def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if post.user != request.user:
        return redirect('group_purchase:home')

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.item_name = request.POST['item_name']
        post.price = request.POST['price']
        post.max_participants = request.POST['max_participants']
        post.location = request.POST['location']

        if 'photo' in request.FILES:
            post.photo = request.FILES['photo']

        post.save()

    return redirect('group_purchase:detail', post.id)

def join_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    post = get_object_or_404(Post, pk=post_id)

    if post.user != request.user:
        if not post.participants.filter(pk=request.user.pk).exists():
            if post.participants.count() < post.max_participants:
                post.participants.add(request.user)

    return redirect('group_purchase:detail', post.id)

def leave_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    post = get_object_or_404(Post, pk=post_id)

    if post.participants.filter(pk=request.user.pk).exists():
        post.participants.remove(request.user)

    return redirect('group_purchase:detail', post.id)