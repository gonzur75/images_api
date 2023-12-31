from django.contrib.auth import get_user_model
from django.db import models

from images.validators import validate_file_type

User = get_user_model()


# Create your models here.
class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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


class Thumbnail(models.Model):
    image = models.ForeignKey("Image", related_name='thumbnails', on_delete=models.CASCADE)
    url = models.FileField(upload_to='resized_images/')
    size = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.url.name}"
