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


class PageNumberViewSet(ExampleViewSet):
    pagination_class = hedju.HeaderPageNumberPagination
    page_size = 100


class CursorViewSet(ExampleViewSet):
    pagination_class = hedju.HeaderCursorPagination


api_router = routers.SimpleRouter()
api_router.register('examples', ExampleViewSet)
api_router.register('limit_examples', LimitOffsetViewSet)
api_router.register('page_examples', PageNumberViewSet)
api_router.register('cursor_examples', CursorViewSet)
