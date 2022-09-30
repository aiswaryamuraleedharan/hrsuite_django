from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('approve/<str:pk>',views.approve,name='approve'),
    path('reject/<str:pk>',views.reject,name='reject')
]