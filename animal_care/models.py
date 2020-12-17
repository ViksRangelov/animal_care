from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=20)
    image_url = models.URLField(null=True)
    description = models.TextField(max_length=250, null=True)
    LOW = 'LOW'
    MEDIUM = 'medium'
    HIGH = 'high'
    PRIORITY_CHOICES = [
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high'),
    ]
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default=LOW,
    )
    is_cured = models.BooleanField(blank=False)
