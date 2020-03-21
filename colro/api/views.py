from django.contrib.auth.models import User, Group

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions, status

from colro.api.serializers import UserSerializer


@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.data['username'],
            serialized.data['email'],
            serialized.data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)