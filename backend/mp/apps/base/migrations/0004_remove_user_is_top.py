# Generated by Django 3.0.4 on 2020-03-24 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_is_top'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_top',
        ),
    ]
