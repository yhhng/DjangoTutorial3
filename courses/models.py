from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_number = models.CharField(max_length=255)
    description = models.TextField(
        blank=True, null=True
    )  # Allows storing a detailed course description and can be null
    credits = models.IntegerField(
        null=True
    )  # Stores the number of credits for the course and can be null
