from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user_id = models.CharField(max_length = 20) #아이디
    name = models.CharField(max_length = 20) #사용자의 이름
    student_Number = models.CharField(max_length=45) #학번
    user_PW = models.CharField(max_length=256) #사용자의 패스워드
    major = models.CharField(max_length=45) #전공
    age = models.IntegerField() #나이
    admin = models.IntegerField() #유저 권환 1: 관리자, 0: 사용자

    def __str__(self):
        return self.name