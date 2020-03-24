from django.db import models

from base.models.base import Base


class Topic(Base):
    user_id = models.IntegerField("用户id")
    content = models.TextField("内容")
    is_top = models.BooleanField("置顶", default=False)
    view_count = models.IntegerField("查看次数", default=0)

    class Meta:
        db_table = "topic"
        verbose_name = "话题"
        verbose_name_plural = "话题"


class Activity(Base):
    user_id = models.IntegerField("用户id")
    title = models.CharField("标题", max_length=128)
    content = models.TextField("内容")
    start_time = models.DateTimeField("开始时间")
    end_time = models.DateTimeField("结束时间")
    place = models.TextField("地点")
    contact_wx = models.CharField("微信", max_length=32)
    is_top = models.BooleanField("置顶", default=False)
    view_count = models.IntegerField("查看次数", default=0)

    class Meta:
        db_table = "activity"
        verbose_name = "活动"
        verbose_name_plural = "活动"

    def __str__(self):
        return self.title

