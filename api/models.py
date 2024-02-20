from django.db import models


class StudentRegister(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hobby = models.CharField(max_length=30)

    def __str__(self):
        return self.name
