import pytest

from images.serializers import ThumbnailGeneratorSerializer



@pytest.mark.serializers
def test_wrong_size_data_type(db, user, create_test_thumbnail_serializer_data, remove_test_data):
    create_test_thumbnail_serializer_data['sizes'] = ['not_an_int']

    serializer = ThumbnailGeneratorSerializer(data=create_test_thumbnail_serializer_data,
                                              context={'user': user})

    assert not serializer.is_valid()

    assert set(serializer.errors) == {'sizes'}
