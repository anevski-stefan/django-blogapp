# Generated by Django 4.1.7 on 2023-06-02 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0007_postcomments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomments',
            name='title_comment',
        ),
    ]