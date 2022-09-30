from django.urls import path
from .import views

urlpatterns = [
    path('',views.Employee,name='employee'),
    path('register/',views.Home,name='home'),
    path('update/<str:pk>',views.Update,name='update'),
    path('delete/<str:pk>',views.DeleteUser,name='delete')
] 