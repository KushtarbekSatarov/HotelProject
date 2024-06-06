from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/', CustomSignupView.as_view(), name='signup'),

    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

    path('hotel/', HotelViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='hotel_list'),
    path('hotel/<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='hotel_detail'),

    path('roomtype/', RoomTypeViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='roomtype_list'),
    path('roomtype/<int:pk>/', RoomTypeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='roomtype_detail'),

    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='booking_list'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='booking_detail'),

    path('reviews/', ReviewsViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='reviews_list'),
    path('reviews/<int:pk>/', ReviewsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='reviews_detail'),

    path('hotelimage/', HotelImageViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='hotelimage_list'),
    path('hotelimage/<int:pk>/', HotelImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='hotelimage_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='favorite_list'),
    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='favorite_detail'),

]