# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .serializers import UserSerializer
# from rest_framework.authtoken.models import Token
# from .serializers import UserSerializer
#
# class UserAuthenticationView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#///////////////////////////////

# from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics, status, request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from . import models
from django.shortcuts import get_object_or_404, render

from rest_framework.views import APIView
from rest_framework import generics, status

from .models import Posts
from .serializers import PostSerializer


from rest_framework import generics, permissions
from rest_framework.response import Response



# class UserCreateView(generics.CreateAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = UserSerializer

from django.http import HttpResponseForbidden


class UserCreateView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    #
    # def post(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseForbidden('You must be logged in to access this page.')
    #
    #     return super().post(request, *args, **kwargs)

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()
    # queryset = models.auth_user.objects.all()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        user_id = self.kwargs['user_id']
        obj = get_object_or_404(models.User, id=user_id)
        return obj

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostCreateView(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer




class PostDetailView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

class PostUpdateView(generics.UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

class PostDeleteView(generics.DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'




# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from .serializers import UserSerializer, UserLoginSerializer
# from . import models

# class UserCreateView(generics.CreateAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserLoginView(generics.CreateAPIView):
#     serializer_class = UserLoginSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key}, status=status.HTTP_200_OK)
#


