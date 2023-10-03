import os

from PIL import Image

from config import settings


def thumbnail_create(image, size):
    img = Image.open(image.url)
    size_percent = (size / float(img.size[1]))
    width = int(img.size[0] * size_percent)

    img.thumbnail((width, size))
    path = settings.MEDIA_ROOT + 'resized_images'

    os.makedirs(path, exist_ok=True)
    filename = image.name.replace(' ', '_')
    splitext = os.path.splitext(filename)
    new_filename = f'{splitext[0]}_{size}{splitext[1]}'
    filepath = path + os.path.sep + new_filename

    img.save(filepath)

    return new_filename
