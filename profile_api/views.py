from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers


class HelloApiView(APIView):
    """Test Api View"""
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIVie features"""
        an_apiview = [
            "Uses HTTP methods as function (get,put,delete,put)",
            "Is similar to traditional Django view",
            "Gives you the most control over application logic",
            "Is mapped manually to URL"
        ]

        return Response({
            'message': 'Hello !',
            'an_apiview': an_apiview
        })

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST

                            )


    def put(request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self,request, pk=None):
        """Handle partial request of an object"""
        return Response({'method': 'PATCH'})

    def delete(self,request, pk=None):
        """Handle partial request of an object"""
        return Response({'method': 'DELETE'})
