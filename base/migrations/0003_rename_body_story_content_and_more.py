# Generated by Django 4.0.3 on 2022-03-31 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_summary_story_preview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='preview',
            new_name='summary',
        ),
    ]