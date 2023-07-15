from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=150)
    emp_code = models.CharField(max_length=50)
    mobile = models.PositiveBigIntegerField()
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
