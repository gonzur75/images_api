import pytest

from conftest import test_exp_link_serializer_data
from expiring_links.serializers import ExpiringLinkSerializer


@pytest.mark.serializers
def test_wrong_data_type(db, user, remove_test_data, test_exp_link_serializer_data):
    test_exp_link_serializer_data['image_id'] = 2
    test_exp_link_serializer_data['expiration_time'] = 299

    serializer = ExpiringLinkSerializer(data=test_exp_link_serializer_data,
                                        context={'user': user})

    assert not serializer.is_valid()

    assert set(serializer.errors) == {'image_id', 'expiration_time'}
