from rest_framework import serializers
from authentication.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Args: User object, serializer json object sent in validated_data dictionary
        """
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
        
    class Meta:
        model = User
        fields = '__all__'
