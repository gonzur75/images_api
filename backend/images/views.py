import os.path

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from config import settings
from images import serializers
from images.helpers import thumbnail_create
from images.models import Image, Thumbnail
from images.serializers import ImageSerializer, ThumbnailGeneratorSerializer, ThumbnailSerializer


class ImageViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer

    @method_decorator(cache_page(60 * 5))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'create_thumbnails':
            return ThumbnailGeneratorSerializer
        return ImageSerializer

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

    @action(methods=['post'], detail=False)
    def create_thumbnails(self, request):

        result = ThumbnailGeneratorSerializer(data=request.data, context={'user': request.user})
        if result.is_valid():
            thumbnail_sizes = result.data.get('sizes')
            image = Image.objects.get(author=request.user, pk=result.data.get('image_id'))
            thumbnails_sizes_in_db = [thumbnail.size for thumbnail in Thumbnail.objects.filter(image=image)]
            thumbnail_urls = []
            for thumbnail_size in thumbnail_sizes:
                if thumbnail_size not in thumbnails_sizes_in_db:
                    thumbnail = thumbnail_create(image, thumbnail_size)
                    thumbnail_url = os.path.join('resized_images', thumbnail)
                    Thumbnail.objects.create(image=image, url=thumbnail_url, size=thumbnail_size)
                    thumbnail_urls.append(thumbnail_url)
                else:
                    thumbnail_urls.append(Thumbnail.objects.get(image_id=image.pk, size=thumbnail_size))

            thumbnail_absolute_urls = [f'{request.build_absolute_uri(settings.MEDIA_URL)}{url}' for url in
                                       thumbnail_urls]
            if request.user.account.has_link:
                original_image = f'{request.build_absolute_uri(settings.MEDIA_URL)}{image.url}'
                return Response({'thumbnails': thumbnail_absolute_urls, 'original_image': original_image})
            return Response({'thumbnails': thumbnail_absolute_urls})

        return Response(result.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def retrieve_thumbnails(self, request, pk=None):
        image = Image.objects.filter(pk=pk, author=request.user)
        if not image:
            raise ValidationError(f'Opps! Could not find image with id {pk}')
        queryset = Thumbnail.objects.filter(image__author=request.user, image_id=pk)
        serializers = ThumbnailSerializer(queryset, many=True, context={"request": request})
        return Response(serializers.data)

