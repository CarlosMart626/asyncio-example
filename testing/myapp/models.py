from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=140)
    created = models.BooleanField(default=True)
