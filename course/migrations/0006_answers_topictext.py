# Generated by Django 5.0.1 on 2024-03-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_remove_answers_prgrscontribution_userprogress'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='topictext',
            field=models.TextField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]