from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Property, Review

class PropertySerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        fields = '__all__'
        model = Property


class ReviewSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        fields = '__all__'
        model = Review

