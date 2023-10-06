from rest_framework import status

from rest_framework.test import force_authenticate

from conftest import api_request_factory
from images.models import Image
from images.serializers import ImageSerializer
from images.views import ImageViewSet


def test_view_list_images_found(db, api_request_factory, user):
    url = "api/v1/images/1"
    view = ImageViewSet.as_view({"get": "list"})

    request = api_request_factory.get(url)
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == status.HTTP_200_OK


def test_view_create_image(db, api_request_factory, image, user):
    url = "api/v1/images/1"
    view = ImageViewSet.as_view({"post": "create"})
    image_ = {
        "name": "test name",
        "url": image,
    }
    request = api_request_factory.post(url, data=image_, format="multipart")
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == status.HTTP_201_CREATED
    image = Image.objects.first()
    serializer = ImageSerializer(image)
    assert serializer.data == response.data


def test_view_create_image_with_invalid_data(db, api_request_factory, image, user):
    url = "api/v1/images/1"
    view = ImageViewSet.as_view({"post": "create"})
    image_ = {}

    request = api_request_factory.post(url, data=image_, format="multipart")
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert str(response.data["url"][0]) == 'No file was submitted.'
