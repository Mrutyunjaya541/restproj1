from django.db import models

class Student(models.Model):
    Sname = models.CharField(max_length=60)
    Srollno = models.IntegerField()
    Saddr = models.CharField(max_length=60)

    def __str__(self):
        return self.Sname
