# Generated by Django 3.2.5 on 2021-07-28 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataApis', '0018_alter_questionnaire_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='dataApis.form'),
        ),
    ]
