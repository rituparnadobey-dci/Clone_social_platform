from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile, name='profile'),  # Added trailing slash
    path('profile/<int:pk>/follow_unfollow/', views.follow_unfollow, name='follow_unfollow'),
]
