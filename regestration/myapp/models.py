from django.db import models

# Create your models here.

class data(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.name
