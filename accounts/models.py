from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

    age = models.PositiveIntegerField(null=True, blank=True)

    GENDER_CHOICES = [ #M,F는 DB에 저장되는 값 / 남자, 여자는 화면에 보여지는 값
        ('M', '남자'),
        ('F', '여자'),
    ]
    #드롭다운 형태로 보여지도록
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True) 

    phone_number = models.CharField(max_length=20, blank=True)
