# Generated by Django 3.0.4 on 2020-04-01 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnarie', '0002_auto_20200327_1422'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionnarieRecord',
            new_name='QuestionnaireRecord',
        ),
        migrations.AlterModelTable(
            name='questionnairerecord',
            table='questionnaire_record',
        ),
    ]
