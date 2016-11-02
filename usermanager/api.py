"""Api File for usermanager app."""

from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


class UserList(APIView):
    """List all users, or create a new user."""

    def get(self, request, format=None):
        """Get method for UserList to view all users."""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Post method for UserList to create new users."""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request.data)
            response = {'success': True, 'data': serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {'success': False, 'data': serializer.errors}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserQuery(APIView):
    """List all users, or create a new user."""

    def get(self, request, term, format=None):
        """Get method for UserList to view all users."""
        users = User.objects.filter(
            Q(username__icontains=term) |
            Q(first_name__icontains=term) |
            Q(last_name__icontains=term) |
            Q(email__icontains=term)).exclude(pk=request.user.pk)[:10]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
