# Generated by Django 3.1.1 on 2020-09-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_portal', '0003_auto_20200908_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(default='/default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='userstate',
            name='profile_image',
            field=models.ImageField(default='/default.png', upload_to=''),
        ),
    ]