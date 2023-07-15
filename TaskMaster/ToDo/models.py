from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  title
#  status
#  date - current
#  user
#  priority


class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    priority_choices = [
        ('1', 'High'),
        ('2', 'Medium'),
        ('3', 'Low'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=priority_choices)
