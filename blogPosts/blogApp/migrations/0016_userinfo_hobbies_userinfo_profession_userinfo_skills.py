# Generated by Django 4.1.7 on 2023-06-02 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0015_rename_files_blogpost_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='hobbies',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='profession',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='skills',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
