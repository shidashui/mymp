from django.db import models

from base.models.base import Base

class SaveMixin:
    @classmethod
    def add(cls, **kwargs):
        m = cls()
        for name, value in kwargs.items():
            if value:
                setattr(m, name, value)
        m.save()
        return m



class Questionnaire(Base, SaveMixin):
    # email = models.EmailField("邮箱")
    user_id = models.IntegerField("用户id", default=0)
    name = models.CharField("问卷名", max_length=128)
    brief = models.TextField("简介")

    class Meta:
        db_table = 'questionnaire'
        verbose_name = "问卷"
        verbose_name_plural = "问卷"

class QuestionnaireField(models.Model, SaveMixin):
    questionnaire_id = models.IntegerField("问卷id")
    content = models.TextField("题目内容")
    is_multiple = models.BooleanField("多选", default=False)

    class Meta:
        db_table = 'questionnaire_field'

class QuestionnaireChoiceField(models.Model, SaveMixin):
    number = models.IntegerField("序号")
    field_id = models.IntegerField("题目id")
    content = models.TextField("选项内容")

    class Meta:
        db_table = "questionnaire_choice_field"

class QuestionnaireRecord(Base, SaveMixin):
    email = models.EmailField("提交人邮箱")
    questionnaire_id = models.IntegerField("问卷id")
    field_id = models.IntegerField("题目id")
    result = models.CharField("所选内容",max_length=32)

    class Meta:
        db_table = "questionnaire_record"