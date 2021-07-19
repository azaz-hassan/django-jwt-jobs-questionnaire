# Generated by Django 3.2.5 on 2021-07-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('type', models.CharField(max_length=10)),
                ('score', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('optional', models.BooleanField()),
            ],
        ),
    ]
