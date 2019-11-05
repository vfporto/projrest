from rest_framework.serializers import ModelSerializer

from reviews.models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'usuario', 'comentario', 'nota', 'data')