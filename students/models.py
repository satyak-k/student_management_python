from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    admission_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.student_name

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

from django.utils import timezone