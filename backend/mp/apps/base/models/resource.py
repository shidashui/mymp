from django.db import models

from base.models.base import Base


class Image(Base):
    user_id = models.IntegerField("用户id")
    path = models.ImageField("图片", upload_to="img")
    item_code = models.CharField("条目码", max_length=16)

    class Meta:
        db_table = "image"
        verbose_name = "图片"
        verbose_name_plural = "图片"