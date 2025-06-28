from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tecnology = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    