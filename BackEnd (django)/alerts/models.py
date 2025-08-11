from django.db import models

class Alert(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    image = models.ImageField(upload_to='alerts/images/')
    link_in_google_map = models.CharField(max_length=300)
    address = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
