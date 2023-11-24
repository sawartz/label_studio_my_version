from django.db import models

# Create your models here.
class Assignment(models.Model):
    project_id = models.IntegerField(null=True)
    assigned_to = models.CharField(max_length=100)
    def __str__(self):
        return f"project_id: {self.project_id}, assigned_to: {self.assigned_to}"
