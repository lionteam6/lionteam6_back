from django.urls import path
from .views import *

app_name = 'group_purchase'
urlpatterns = [
  path('', home, name='home'),

  path('post/<int:post_id>/<int:user_id>/', detail, name='detail'),

  path('new/<int:user_id>', new, name="new"),
  path('create/<int:user_id>', create, name="create"),

  path('join/<int:post_id>/<int:user_id>/', join_post, name='join_post'),
  path('leave/<int:post_id>/<int:user_id>/', leave_post, name='leave_post'),

  path('delete/<int:post_id>', delete, name="delete"),
  path('update_page/<int:post_id>', update_page, name="update_page"),
  path('update_post/<int:post_id>', update_post, name="update_post"),
]