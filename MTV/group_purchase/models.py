from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE
    )  # 작성자

    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, upload_to="post_photo")
    content = models.TextField(max_length=500)

    item_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    max_participants = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    participants = models.ManyToManyField( settings.AUTH_USER_MODEL, related_name='joined_posts', blank=True
    )  # 참여자

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def participant_count(self):
        return self.participants.count()

    def is_full(self):
        return self.participants.count() >= self.max_participants



