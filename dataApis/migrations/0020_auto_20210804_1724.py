# Generated by Django 3.2.5 on 2021-08-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApis', '0019_alter_questionnaire_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='todo_data',
            new_name='note',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='is_done',
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.TextField(default='hehe'),
            preserve_default=False,
        ),
    ]
