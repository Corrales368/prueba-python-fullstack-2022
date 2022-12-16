# Import django
from rest_framework import serializers

# Import self app
from apps.film.models import Category, Film, FilmUser


class CategorySerializers(serializers.ModelSerializer):
    """
    Serializers for model Category
    """
    class Meta:
        model = Category
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    """
    Serializer for model Film
    """
    category = CategorySerializers()
    # avg_rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Film
        fields = '__all__'  


class FilmUserSerializer(serializers.ModelSerializer):
    """
    Serializer for model FilmUser
    """
    film = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = FilmUser
        fields = '__all__'

