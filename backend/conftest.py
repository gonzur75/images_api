import os
import shutil

import pytest
from django.contrib.auth import get_user_model

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIRequestFactory

from images.models import Image
from config import settings
from django.test import override_settings

from users.models import ThumbnailSize, Account


@pytest.fixture(scope='function')
def user(db,  account_db):
    user = get_user_model().objects.create_user(
        username='testUser',
        password='testPass123',
        email="testuser@test.com",
        account=account_db
    )
    return user


@pytest.fixture
def remove_test_data():
    yield shutil.rmtree(os.path.join(settings.BASE_DIR, 'test_dir'), ignore_errors=True)


@pytest.fixture
@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test_dir', '/media'))
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


@pytest.fixture()
def create_test_thumbnail_serializer_data(db, image_handler):
    image = next(image_handler)
    serializer_data = {
        'image_id': image.pk,
        'sizes': [200]
    }
    return serializer_data


@pytest.fixture(scope='function')
def thumbnail_size_handler(db):
    thumbnail = ThumbnailSize.objects.create(
        size=200,
    )
    return thumbnail


@pytest.fixture(scope='function')
def account_db(db, thumbnail_size_handler):
    size = thumbnail_size_handler
    account = Account.objects.create(
        name='test_Account'
    )
    account.thumbnail_sizes.add(size)
    return account


@pytest.fixture(scope='function')
def test_exp_link_serializer_data(image_handler):
    image = next(image_handler)
    return {
        'image_id': image.id,
        'expiration_time': 500
    }
