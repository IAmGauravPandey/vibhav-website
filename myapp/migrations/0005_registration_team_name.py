# Generated by Django 2.1.4 on 2018-12-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='team_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
