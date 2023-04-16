from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

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