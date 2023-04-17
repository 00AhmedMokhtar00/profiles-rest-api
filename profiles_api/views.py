from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView):
    """Test Api View"""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
             'Gives you the most control over your application logic',
             'Is mapped manually to URLs'
        ]
        
        return Response({
            'message': 'Hello from my first api!',
            'an_apiview': an_apiview
        })
        
    def post(self, request):
        """Create a hello message with our name"""
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            
            return Response({
                'status': status.HTTP_200_OK,
                'message': message
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle partially updating an object"""
        return Response({'method': 'PACH'})
    
    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({'method': 'DELETE'})
    

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Return a hello message"""
        
        a_viewset = [
            'Uses actions: list, create, retrieve, update, partially_update and destroy',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        
        return Response({
            'a_viewset': a_viewset,
            'status': status.HTTP_200_OK
        })
        
    def create(self, request):
        """Create a new hello message"""
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            
            return Response({
                'status': status.HTTP_200_OK,
                'message': message
            })
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object by its ID"""
        
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle partially updating an object by its ID"""
        
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle deleting an object by its ID"""
        
        return Response({'http_method': 'DELETE'})
    
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    
    serializer_class = serializers.UserProfileSeralizer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')
    
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES