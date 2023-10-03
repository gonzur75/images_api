import os.path

import pytest

from config import settings
from conftest import image_handler
from images.models import Image, Thumbnail

from django.test import override_settings


@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test_dir', 'media'))
@pytest.mark.models
def test_image_creation(image_handler, remove_test_data):
    image_handler = next(image_handler)
    assert isinstance(image_handler, Image)
    assert image_handler.author.username == 'testUser'
    assert image_handler.url.url == '/media/images/test_file.jpg'
    assert image_handler.name == 'test_file.jpg'
    assert str(image_handler) == 'test_file.jpg'


@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test_dir', 'media'))
@pytest.mark.models
def test_thumbnail_fields(image_handler, image):
    image_handler = next(image_handler)
    thumbnail = Thumbnail.objects.create(
        image=image_handler,
        url=image,
        height=43
    )
    assert [*vars(thumbnail)] == ['_state', 'id', 'image_id', 'url', 'height']