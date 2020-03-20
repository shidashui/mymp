from django.db import models


class Base(models.Model):
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self):
        name = self.__class__.__name__
        s = ''
        for attr, value in self.__dict__.items():
            if not attr.startswith('_'):
                s += '{}: ({})\n'.format(attr, value)
        return '< {}\n{} >\n'.format(name, s)

class Dict(Base):
    item_name = models.CharField('字典名', max_length=16)
    item_code = models.CharField('字典码', max_length=16)

    class Meta:
        db_table = "dict"
        verbose_name = "条目"
        verbose_name_plural = "条目"

    def __str__(self):
        return self.item_name