from django.db import models

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
