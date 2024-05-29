# Generated by Django 5.0.6 on 2024-05-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_followers_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_picture/default_profile_picture.webp', null=True, upload_to='profile_picture', verbose_name='profile picture'),
        ),
    ]
