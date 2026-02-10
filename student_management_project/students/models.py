from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)            # Student's full name
    age = models.PositiveIntegerField()                 # Student's age
    course = models.CharField(max_length=100)          # Course enrolled
    email = models.EmailField(unique=True)              # Student email
    def __str__(self):
        return self.name
