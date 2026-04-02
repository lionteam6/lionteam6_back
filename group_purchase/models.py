from django.db import models

class User(models.Model): #기본적인 User 모델 클래스만 생성
  user_name = models.CharField(max_length=20)
  password = models.CharField(max_length=128)
  email = models.EmailField()

  def __str__(self):
    return self.user_name

class Post(models.Model):
  user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE) #작성자 필드 (1:N)
  title = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  photo = models.ImageField(blank=True, null=True, upload_to="post_photo")
  content = models.TextField(max_length=500)
  
  #추가 필드
  item_name = models.CharField(max_length=100)   # 공구 품목
  price = models.PositiveIntegerField()          # 가격
  max_participants = models.PositiveIntegerField()  # 인원
  location = models.CharField(max_length=100)    # 장소

  #참여자 필드
  participants = models.ManyToManyField(User, related_name='joined_posts', blank=True)

  def __str__(self):
    return self.title
  
  def summary(self):
    return self.content[:100] #게시글 앞 100글자만 보여주는 함수
  
  def participant_count(self) :  #현재 참여 인원 수
    return self.participants.count()
  
  def is_full(self): # 모집 마감 여부
    return self.participants.count() >= self.max_participants




