# Generated by Django 3.1.1 on 2020-09-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_portal', '0004_auto_20200908_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='userstate',
            name='profile_image',
            field=models.ImageField(upload_to=''),
        ),
    ]