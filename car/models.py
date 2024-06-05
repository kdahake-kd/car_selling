from django.db import models

class carList(models.Model):
    name=models.CharField(max_length=256)
    description=models.CharField(max_length=256)
    active=models.BooleanField(default=False)
    

