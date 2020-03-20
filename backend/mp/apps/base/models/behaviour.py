from base.models.base import Base
from django.db import models

class Like(Base):
    user_id = models.IntegerField("用户id")
    item_code = models.CharField("条目码", max_length=16)

    class Meta:
        db_table = "like"
        verbose_name = "点赞"
        verbose_name_plural = "点赞"

class Collect(Base):
    user_id = models.IntegerField("用户id")
    item_code = models.CharField("条目码", max_length=16)

    class Meta:
        db_table = "collect"
        verbose_name = "收藏"
        verbose_name_plural = "收藏"

class Comment(Base):
    user_id = models.IntegerField("用户id")
    content = models.TextField("内容")
    item_code = models.CharField("条目码", max_length=16)
    father_id = models.IntegerField("父评论")

    class Meta:
        db_table = "comment"
        verbose_name = "评论"
        verbose_name_plural = "评论"