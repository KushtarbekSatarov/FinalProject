from django.urls import path
from .views import *

urlpatterns  = [
    path('accounts/signup/', CustomSignupView.as_view(), name='signup'),

    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('carmake/', CarMakeViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='carmake_list'),
    path('carmake/<int:pk>/', CarMakeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='carmake_detail'),

    path('model/', ModelViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='model_list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='model_detail'),

    path('car/', CarViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='car_list'),
    path('car/<int:pk>/', CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='car_detail'),

    path('bet/', BetViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='bet_list'),
    path('bet/<int:pk>/', BetViewSet.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'}),
         name='bet_detail'),

    path('comment/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'}),
         name='comment_detail'),
]