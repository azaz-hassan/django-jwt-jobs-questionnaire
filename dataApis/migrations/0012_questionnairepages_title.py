# Generated by Django 3.2.5 on 2021-07-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApis', '0011_questionnairepages'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnairepages',
            name='title',
            field=models.CharField(default='Big Fan', max_length=64),
        ),
    ]
