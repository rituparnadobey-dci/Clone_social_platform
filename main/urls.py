from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile, name='profile'),  # Added trailing slash
    path('profile/<int:pk>/follow_unfollow/', views.follow_unfollow, name='follow_unfollow'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
<<<<<<< HEAD
    path('update_user/', views.update_user, name='update_user'),
=======
>>>>>>> fd877cdb32189e5b3d46a56dddb8269e45b7384e
]
