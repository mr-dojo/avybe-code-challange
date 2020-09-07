from django.db import models


class Person(models.Model):
    nickname = models.CharField(max_length=30)

    def __str__(self):
        return self.nickname
