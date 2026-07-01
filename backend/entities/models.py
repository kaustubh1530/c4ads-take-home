from django.db import models

class Entity(models.Model):
    ENTITY_TYPE_CHOICES = [
        ('Individual', 'Individual'),
        ('Organization', 'Organization'),
    ]

    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=50, choices=ENTITY_TYPE_CHOICES)
    date_added = models.DateField()
    program = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name