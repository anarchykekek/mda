from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField("Name", max_length=20)
    age = models.IntegerField("Age")
    area = models.CharField("Area", max_length=40)
    address = models.CharField("Address", max_length=40)

    def __str__(self):
        return self.name

