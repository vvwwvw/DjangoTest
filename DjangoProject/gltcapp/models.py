from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

 #모델을 정의 모델 = 객체(object)
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
# 속성


    def publish(self):
        self.published_date = timezone.now()
        self.save()
# 메소드

    def __str__(self):
        return self.title

