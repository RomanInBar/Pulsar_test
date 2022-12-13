from rest_framework import serializers

from .models import Product
from .utils import converter


class ImageSerializer(serializers.ModelSerializer):
    """Сериалайзер для изображений."""

    path = serializers.SerializerMethodField(read_only=True)
    formats = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ('path', 'formats')

    def get_path(self, obj):
        return str(obj).split('.')[0]

    def get_formats(self, obj):
        original_format = str(obj).split('.')[1]
        obj = converter(obj)
        new_format = str(obj).split('.')[1]
        return [original_format, new_format]


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер объектов модели Product."""

    image = ImageSerializer()
    status = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'article', 'price', 'status', 'image')

    def get_status(self, obj):
        return obj.get_status_display()
