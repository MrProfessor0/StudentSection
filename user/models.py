from django.db import models

# Create your models here.

"""
Sections Model
"""
class Section(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name


"""
Student Model
"""
class Student(models.Model):
    name = models.CharField(max_length=255)
    section = models.ForeignKey(Section, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
