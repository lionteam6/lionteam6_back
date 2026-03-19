from django import forms
from .models import Post

class PostForm(forms.ModelForm) :
  class Meta:
    model=Post
    fields=['title', 'content', 'item_name', 'price', 'max_participants', 'location']