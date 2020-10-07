from rest_framework.serializers import ModelSerializer
from .models import MovieModel, RatingModel


class MovieSerializer(ModelSerializer):
    class Meta:
        model = MovieModel
        fields = '__all__'
