# Generated by Django 4.1.7 on 2023-06-02 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0013_userinfo_blockedusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
