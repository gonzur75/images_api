from rest_framework import status

from expiring_links.models import ExpiringLink
from expiring_links.serializers import ExpiringLinkSerializer
from expiring_links.views import ExpiringLinkViewSet
from rest_framework.test import force_authenticate


def test_view_create_expiring_link(db, api_request_factory, image, user, test_exp_link_serializer_data):
    url = "api/v1/expiring_links"
    view = ExpiringLinkViewSet.as_view({"post": "create"})
    data_ = test_exp_link_serializer_data
    request = api_request_factory.post(url, data=data_, format="multipart")
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == status.HTTP_201_CREATED
    assert ExpiringLink.objects.count() == 1
