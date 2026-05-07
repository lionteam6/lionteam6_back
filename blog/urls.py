from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view()), #전체 조회
    path('<int:pk>/', PostDetailView.as_view()), #특정 object 조회
]