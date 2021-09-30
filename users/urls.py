from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.logout_user, name='log_out'),
    path('update_profile/', views.create_profile, name='create_profile'),
    path('profile_card/', views.generate_profile, name='generate_profile'),
]
