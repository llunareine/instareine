# from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
# from .views import UserLoginView, UserCreateView

# urlpatterns = [
#     path('authenticate/', UserAuthenticationView.as_view(), name='user_authenticate'),
#     path('token-auth/', obtain_auth_token, name='api_token_auth'), # Optional token auth endpoint
# ]

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserCreateView, UserLoginView, UserDetail, UserList, PostListCreateAPIView

from django.urls import path
from .views import (
    PostCreateView,
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
)


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user_create'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'), # Optional token auth endpoint
    path('users', UserList.as_view(), name='users'),
    path('users/<int:user_id>', UserDetail.as_view(), name='user_id'),

    # path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:id>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:id>/delete/', PostDeleteView.as_view(), name='post-delete'),


]
