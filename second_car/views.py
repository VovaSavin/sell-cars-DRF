from rest_framework.response import Response
from .serializers import (
    ListCarsSeralizers,
    DetailCarsSeralizers,
    ListCategorySeralizer,
    DetailCategorySeralizer,
    CreateCarSeralizers
)
from rest_framework import generics
from rest_framework.views import APIView
from .models import CarAdvertisement, Category


class ListCategoryView(APIView):
    """Список кузовов авто"""

    def get(self, request):
        categories = Category.objects.all()
        serializer = ListCategorySeralizer(categories, many=True)
        return Response(serializer.data)


class DetailCategoryView(APIView):
    """Список кузовов авто"""

    def get(self, request, slug):
        categories = Category.objects.get(body=slug)
        serializer = DetailCategorySeralizer(categories)
        return Response(serializer.data)


class ListCarAdvertApi(APIView):
    """Список объявлений"""

    def get(self, request):
        cars = CarAdvertisement.objects.all()
        serializer = ListCarsSeralizers(cars, many=True)
        return Response(serializer.data)


class DetailCarAdvertApi(APIView):
    """Одно обьявление"""

    def get(self, request, pk):
        car = CarAdvertisement.objects.get(id=pk)
        serializer = DetailCarsSeralizers(car)
        return Response(serializer.data)


class CreateAdvertView(APIView):
    """Создание объявления"""

    def post(self, request):
        advert = CreateCarSeralizers(data=request.data)
        if advert.is_valid():
            advert.validated_data["author"] = self.request.user
            advert.save()
        return Response(status=201)
