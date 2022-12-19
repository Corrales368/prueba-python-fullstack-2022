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
    class Meta:
        model = Film
        fields = '__all__'  
    
    def to_representation(self, instance):
        return {
            'pk' : instance.pk,
            'name' : instance.name,
            'category' :instance.category.name,
            'type' : instance.type
        }


class FilmUserSerializer(serializers.ModelSerializer):
    """
    Serializer for model FilmUser
    """
    class Meta:
        model = FilmUser
        fields = '__all__'
    
    def create(self, validated_data):
        """
        Override method create for try except error compound key
        """
        try:
            return super().create(validated_data)
        except:
            raise serializers.ValidationError("You cannot create this record, since you already have a rating created for this film")

