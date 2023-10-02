import pytest

from users.models import Customer


@pytest.mark.django_db
def test_create_customer(user, django_user_model):
    user = Customer.objects.create(
        user=user,
        plan=1
    )
    saved_user = django_user_model.objects.get(email="testuser@test.com")

    assert saved_user.username == "testUser"
