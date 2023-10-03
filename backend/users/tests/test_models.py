import pytest

from conftest import account_db
from users.models import Customer, ThumbnailSize


@pytest.mark.django_db
def test_create_customer(user, account_db, django_user_model):
    user = Customer.objects.create(
        user=user,
        account=account_db
    )
    saved_user = django_user_model.objects.get(email="testuser@test.com")

    assert saved_user.username == "testUser"


@pytest.mark.django_db
def test_create_account(account_db):
    assert account_db.name == "Basic"
    assert account_db.thumbnail_sizes.count() == 1
    assert str(account_db) == "Basic"


@pytest.mark.django_db
def test_create_thumbnail(thumbnail_size_handler):
    thumbnail = thumbnail_size_handler
    assert thumbnail.name == "200px"
    assert ThumbnailSize.objects.count() == 1
    assert str(thumbnail) == "200px"
