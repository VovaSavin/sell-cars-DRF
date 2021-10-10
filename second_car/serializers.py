from rest_framework import serializers
from .models import CarAdvertisement, Category, ImageCars


class ListImgSeralizers(serializers.ModelSerializer):
    """Список изображений авто"""
    car = serializers.SlugRelatedField(slug_field="brand", read_only=True)

    class Meta:
        model = ImageCars
        exclude = ["id", ]


class ListCarsSeralizers(serializers.ModelSerializer):
    """Сериализатор для вывода списка авто"""
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    car_photo = ListImgSeralizers(many=True)

    class Meta:
        model = CarAdvertisement
        fields = ["id", "header", "brand", "model_car", "author", "car_photo", ]


class DetailCarsSeralizers(serializers.ModelSerializer):
    """Сериализатор для вывода одного авто"""
    typeauto = serializers.SlugRelatedField(slug_field="body", read_only=True)
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = CarAdvertisement
        exclude = ["id", ]


class CreateCarSeralizers(serializers.ModelSerializer):
    """Создание обьявления"""

    class Meta:
        model = CarAdvertisement
        exclude = [
            "id", "author",
        ]


class ListCategorySeralizer(serializers.ModelSerializer):
    """Список кузовов авто"""

    class Meta:
        model = Category
        fields = ["id", "body"]


class DetailCategorySeralizer(serializers.ModelSerializer):
    """Один кузов авто"""
    typeauto = ListCarsSeralizers(many=True)

    class Meta:
        model = Category
        fields = ["id", "body", "typeauto"]
