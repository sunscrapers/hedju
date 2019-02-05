from rest_framework import routers
from rest_framework import serializers
from rest_framework import viewsets

import hedju
from .models import Example


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = '__all__'


class ExampleViewSet(viewsets.ModelViewSet):
    serializer_class = ExampleSerializer
    queryset = Example.objects.all()


class LimitOffsetViewSet(ExampleViewSet):
    pagination_class = hedju.HeaderLimitOffsetPagination


api_router = routers.SimpleRouter()
api_router.register('examples', ExampleViewSet)
api_router.register('limit_examples', LimitOffsetViewSet)
