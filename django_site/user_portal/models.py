from django.db import models


class Person(models.Model):
    nickname = models.CharField(max_length=30)
    profile_image = models.ImageField()

    def __str__(self):
        return self.nickname


class UserState(models.Model):
    current_user = models.CharField(max_length=30)
    profile_image = models.ImageField()

    def __str__(self):
        return self.current_user
