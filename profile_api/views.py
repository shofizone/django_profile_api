from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profile_api import serializers, models, permissions


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

    def patch(self, request, pk=None):
        """Handle partial request of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle partial request of an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'User action (list, crete, retrieve, update, partial_update)',
            'Automatically map to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({
            'message': 'Hello !',
            'a_viewset': a_viewset
        })

    def create(self, request):
        """Create a new hello message"""

        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name} !'
            return Response({'message': message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting object by its ID"""
        return Response({'http_methode': 'GET'})

    def update(self, request, pk=None):
        """Handle Updating object by its ID"""
        return Response({'http_methode': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partial_update object by its ID"""
        return Response({'http_methode': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_methode': 'DELETE'})


class UserProfileVIewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginAPIView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
