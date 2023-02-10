from django.db import models

class Participant(models.Model):
    full_name = models.CharField(max_length=255)
    pen_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    
    year_and_school = models.TextField(max_length=255)
    submission_file = models.TimeField(max_length=255)
    scores = models.BigIntegerField(default=0)

