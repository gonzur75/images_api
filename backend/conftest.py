import os
import shutil

import pytest

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIRequestFactory

from images.models import Image
from config import settings
from django.test import override_settings

from users.models import ThumbnailSize, Account


@pytest.fixture
def user(db, django_user_model):
    return django_user_model.objects.create_user(
        username='testUser',
        password='testPass123',
        email="testuser@test.com"
    )


@pytest.fixture
def remove_test_data():
    yield shutil.rmtree(os.path.join(settings.BASE_DIR, 'test_dir'), ignore_errors=True)


@pytest.fixture
@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test_dir', 'media'))
def image_handler(db, user):
    image_object = Image.objects.create(
        author=user,
        url=SimpleUploadedFile('test_file.jpg',
                               content=open(os.path.join('test_files', 'test_image.jpeg'), 'rb').read())
    )
    yield image_object


@pytest.fixture
def image():
    yield SimpleUploadedFile('test_file.jpg',
                             content=open(os.path.join('test_files', 'test_image.jpeg'), 'rb').read())


@pytest.fixture
def api_request_factory():
    return APIRequestFactory()


@pytest.fixture
def thumbnail_size_handler(db, user):
    thumbnail = ThumbnailSize.objects.create(
        name='200px',
        size=200,
    )
    return thumbnail


@pytest.fixture()
def account_db(db, thumbnail_size_handler):
    size = thumbnail_size_handler
    account = Account.objects.create(
        name='Basic'
    )
    account.thumbnail_sizes.add(size)
    return account
