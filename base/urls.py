from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-post/', views.createPost, name='create-post'),
    path('sample/', views.sample, name='sample'),
    path('login/', views.loginPage, name='login'),
    path('contact/', views.contact, name='contact'),
    path('logout/', views.logoutPage, name='logout'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('view-post/<str:pk>/', views.viewPost, name='view-post')
]
