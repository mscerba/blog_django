# Generated by Django 4.0.6 on 2022-09-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read Blog Post...', max_length=255),
        ),
    ]
