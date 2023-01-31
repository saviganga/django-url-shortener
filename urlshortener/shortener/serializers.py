from rest_framework import serializers

from shortener import models as shortener_models
from shortener.utils import randomize_strings

class WriteURLShortenerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = shortener_models.URLShortener
        fields = ["original_url",]

    def create(self, validated_data):

        base_url = 'https://ganga.com/'
        random_string = randomize_strings()
        shortened_url = f"{base_url}{random_string}"
        
        shortened_url_obj = self.Meta.model.objects.create(
            original_url=validated_data.get('original_url'),
            shortened_url_code=random_string,
            shortened_url=shortened_url
        )

        return {
            "original_url": shortened_url_obj.original_url,
            "shortened_url": shortened_url_obj.shortened_url,
            "shortened_url_code": shortened_url_obj.shortened_url_code
        }



        



class ReadURLShortenerSerializer(serializers.ModelSerializer):

    class Meta:
        model = shortener_models.URLShortener
        fields = "__all__"


class ResolveShortenedURLSerializer(serializers.Serializer):
    shortened_url = serializers.URLField(required=True, max_length=100)