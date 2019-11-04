from rest_framework.viewsets import ModelViewSet

from reviews.api.serializers import ReviewSerializer
from reviews.models import Review


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
