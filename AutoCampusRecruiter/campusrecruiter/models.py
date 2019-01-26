from django.db import models

class Recruitment(models.Model):

    col_name = models.CharField(max_length=200)
    col_address = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    def __str__(self):
      return self.col_name

class Students(models.Model):
    student_name =  models.CharField(max_length=200)
    student_coll =  models.CharField(max_length=200)
    roll_no = models.CharField(max_length=200)
    student_gpa = models.CharField(max_length=200)
    def __str__(self):
      return self.student_name

