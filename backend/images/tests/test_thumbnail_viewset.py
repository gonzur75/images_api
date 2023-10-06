import pytest
from rest_framework import status
from rest_framework.test import force_authenticate

from images.views import ImageViewSet


@pytest.mark.views
def test_user_can_make_thumbnail(user, api_request_factory, image_handler):
    view = ImageViewSet.as_view({'post': 'create_thumbnails'})
    user = user
    image = next(image_handler)

    request = api_request_factory.post(
        'api/v1/images/create_thumbnails/',
        {
            'image_id': image.pk,
            'sizes': [200]
        },
        format='json'
    )
    force_authenticate(request, user)
    response = view(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data.get('thumbnails')[0] == 'http://testserver/media/resized_images/test_file_200.jpg'
