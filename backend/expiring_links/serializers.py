from rest_framework import serializers

from images.models import Image


class ExpiringLinkSerializer(serializers.Serializer):
    image_id = serializers.IntegerField(min_value=1)
    expiration_time = serializers.IntegerField()

    def validate_user(self, data):
        user = self.context['user']
        if not user.account.has_expiring_link:
            raise serializers.ValidationError('Your account does not allow expiring links')

        return data

    def validate_image_id(self, value):
        user = self.context['user']
        image = Image.objects.filter(pk=value, author=user)

        if not image:
            raise serializers.ValidationError('Ops! Image does not exist')

        return value

    def validate_expiration_time(self, value):
        if not 300 <= value <= 30000:
            raise serializers.ValidationError(
                'Expiration time of more than 300 but less than 30000 seconds is required')

        return value
