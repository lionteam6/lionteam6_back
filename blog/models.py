from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    #작성자필드 (기본 User 참조)
    author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    #사진필드
    content = models.TextField(max_length=500)

    item_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    max_participants = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    # 참여자 필드
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='joined_posts', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    #참여자 카운드 함수
    def participant_count(self):
      return self.participants.count()

    #참여자 다 찼는지 확인하는 함수
    #PR용
    def is_full(self):
      return self.participants.count() >= self.max_participants
