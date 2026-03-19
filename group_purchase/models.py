from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  content = models.TextField(max_length=500)
  
  #추가 필드
  item_name = models.CharField(max_length=100)   # 공구 품목
  price = models.PositiveIntegerField()          # 가격
  max_participants = models.PositiveIntegerField()  # 인원
  location = models.CharField(max_length=100)    # 장소


  def __str__(self):
    return self.title
