# Generated by Django 2.1.4 on 2018-12-20 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20181219_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='event',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Event'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='team_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
    ]