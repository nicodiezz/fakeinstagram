# Generated by Django 5.0.6 on 2024-05-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_customuser_birth_date_customuser_sex_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='sex',
        ),
        migrations.AddField(
            model_name='customuser',
            name='followers_count',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, default=None, to='users.customuser', verbose_name='following'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='following_count',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='customuser',
            name='posts_count',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile_picture', verbose_name='profile picture'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='biography',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='biography'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, default=None, related_name='customuser_set', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, default=None, related_name='customuser_set', to='auth.permission'),
        ),
    ]
