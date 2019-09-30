from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.myblog, name='myblog'),
    path('<int:blog_id>/', views.detail, name='detail'),
] 
