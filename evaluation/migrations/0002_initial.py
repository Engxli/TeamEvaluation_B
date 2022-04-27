# Generated by Django 4.0.4 on 2022-04-27 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('evaluation', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation', to='project.project'),
        ),
    ]
