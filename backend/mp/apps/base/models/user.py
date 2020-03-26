from django.db import models

from base.models.base import Base

class Role(Base):
    name = models.CharField("角色名", max_length=16)
    code = models.CharField("代码", max_length=16)

    class Meta:
        db_table = "role"
        verbose_name = "角色"
        verbose_name_plural = "角色"

    def __str__(self):
        return self.name

class User(Base):
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女"),
        ("", "")
    )
    open_id = models.CharField("标识符", unique=True, max_length=128)
    session_key = models.CharField("会话密钥", max_length=128)
    token = models.CharField("token", max_length=128, default=None)
    # wx userInfo
    nickname = models.CharField("昵称", max_length=32, default=None, blank=True, null=True)
    avatar_url = models.URLField("头像", default=None, blank=True, null=True)
    gender = models.CharField("性别", choices=GENDER_CHOICES, default="", max_length=8)
    country = models.CharField("国家", max_length=32, default=None, blank=True, null=True)
    province = models.CharField("省份", max_length=32, default=None, blank=True, null=True)
    city = models.CharField("城市", max_length=32, default=None, blank=True, null=True)
    language = models.CharField("语言", max_length=32, default=None, blank=True, null=True)
    # auth info
    email = models.EmailField("邮箱", default=None, null=True, blank=True)
    mobile = models.CharField("手机号", max_length=11, null=True, blank=True)
    student_id = models.CharField("学号", null=True, blank=True, max_length=32)
    is_authenticated = models.BooleanField("认证", default=False)
    role_code = models.CharField("角色代码", null=True, blank=True, max_length=16)
    auth_img = models.ImageField("认证图片", upload_to="img/auth", null=True, blank=True)
    school_id = models.IntegerField("学校id", null=True, blank=True)

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = "用户"

class School(Base):
    name = models.CharField("学校名", max_length=32)
    address = models.TextField("地址")

    class Meta:
        db_table = "school"
        verbose_name = "学校"
        verbose_name_plural = "学校"