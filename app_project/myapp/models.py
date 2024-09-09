from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField(blank=True)  # Make message optional by adding blank=True
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # Corrected from _str_ to __str__
        return f'Contact from {self.name}'
# Create your models here.
