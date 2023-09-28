from django.contrib.auth import get_user_model
from django.db import models

from images.validators import validate_file_type


# Create your models here.
class Image(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    url = models.FileField(upload_to='images/', validators=[validate_file_type])

    created = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.url.name
        return super().save(*args, **kwargs)
