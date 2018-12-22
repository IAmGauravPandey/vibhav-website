# Generated by Django 2.1.4 on 2018-12-19 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_registration_team_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='current_user',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='events',
        ),
        migrations.AddField(
            model_name='registration',
            name='current_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='myapp.Event'),
        ),
        migrations.AddField(
            model_name='registration',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]