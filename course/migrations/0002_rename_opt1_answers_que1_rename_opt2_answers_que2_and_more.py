# Generated by Django 5.0.1 on 2024-02-22 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='opt1',
            new_name='que1',
        ),
        migrations.RenameField(
            model_name='answers',
            old_name='opt2',
            new_name='que2',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='opt3',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='opt4',
        ),
    ]