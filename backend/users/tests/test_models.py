import pytest

from conftest import account_db
from users.models import ThumbnailSize


@pytest.mark.django_db
def test_create_account(account_db):
    assert account_db.name == 'test_Account'
    assert account_db.thumbnail_sizes.count() == 1
    assert str(account_db) == 'test_Account'


@pytest.mark.django_db
def test_create_thumbnail(thumbnail_size_handler):
    thumbnail = thumbnail_size_handler
    assert ThumbnailSize.objects.count() == 1
    assert str(thumbnail) == "200px"
