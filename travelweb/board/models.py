from django.db import models
from authentication.models import UserInfo
from schedule.models import Schedule


# 카테고리
class Category(models.Model):
    objects = models.Manager()
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


# 게시글
class Board(models.Model):
    objects = models.Manager()

    user_id = models.ForeignKey(UserInfo, related_name='boarduser', on_delete=models.CASCADE)
    schedule_id = models.ForeignKey(Schedule, null=True, blank=True, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    imgUrl = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    board_content = models.TextField()
    hit = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# 댓글
class Comment(models.Model):
    objects = models.Manager()
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    comment_content = models.TextField()
    comment_date = models.DateTimeField()

    def __str__(self):
        return self.comment_content