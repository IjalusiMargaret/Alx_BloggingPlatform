# Generated by Django 5.0.3 on 2025-03-31 09:08

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_rename_author_comment_user_comment_slug_post_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='author',
            new_name='subscribed_to',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'post')},
        ),
        migrations.AddField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.RemoveField(
            model_name='like',
            name='rating',
        ),
    ]
