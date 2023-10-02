import os

import magic
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from config import settings


def validate_file_type(upload):
    temp_path = f'tmp/{upload.name[2:]}'
    default_storage.save(temp_path, ContentFile(upload.file.read()))
    full_temp_path = os.path.join(settings.MEDIA_ROOT, temp_path)
    file_type = magic.from_file(full_temp_path, mime=True)

    default_storage.delete(temp_path)
    images_types = [f'image/{image_type}' for image_type in settings.IMAGES_TYPES]
    if file_type not in images_types:
        raise ValidationError(f'File type not supported. Use: *.{" ,*.".join(settings.IMAGES_TYPES)} .')
