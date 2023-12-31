from images.models import Image
from rest_framework import serializers

from images.models import Thumbnail


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("id", "name", "url", "created", "update_at")
        read_only_fields = ['name']


class ThumbnailGeneratorSerializer(serializers.Serializer):
    image_id = serializers.IntegerField(min_value=1)
    sizes = serializers.ListField(child=serializers.IntegerField(min_value=1), allow_empty=False)

    def validate_sizes(self, value):
        user = self.context['user']
        customer_sizes = [size.size for size in user.account.thumbnail_sizes.all()]

        for size in value:
            if size not in customer_sizes:
                raise serializers.ValidationError(
                    f'Chosen height ({size} px) is not available in your account ({user.account})'
                )
        return value

    def validate_image_id(self, value):
        user = self.context['user']
        image = Image.objects.filter(pk=value, author=user)

        if not image:
            raise serializers.ValidationError('Image with given id does not exist.')

        return value


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = '__all__'
