from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

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
