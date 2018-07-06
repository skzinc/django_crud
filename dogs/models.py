from django.db import models

class Dogs(models.Model):
    name=models.CharField(max_length=45)
    breed=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
