# Generated by Django 4.0.4 on 2022-04-19 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('semester', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='added_by',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='semester', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
