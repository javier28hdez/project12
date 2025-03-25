from django.db import models

class CommonModel(models.Model):
    date_created = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)