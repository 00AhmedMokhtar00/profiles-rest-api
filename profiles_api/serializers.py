from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field to test our APIView"""
    name = serializers.CharField(max_length=10)
    
class UserProfileSeralizer(serializers.ModelSerializer):
    """Serializer a user profile object"""
    
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }
        
    def create(self, validated_data):
        """Create and return a new user"""
        
        user = models.UserProfile.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        return user
    
    def update(self, instance, validated_data):
        """Handeling update the password to be hashed before storing it"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)
    
    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }
        