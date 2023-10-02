from rest_framework import generics, viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from images.models import Image
from images.serializers import ImageSerializer


class ImageViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(author=user)

    def create(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = serializer.create(
            {**serializer.validated_data, "author": request.user})
        image_serializer = ImageSerializer(image)

        return Response(image_serializer.data, status.HTTP_201_CREATED)
