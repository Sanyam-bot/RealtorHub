from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('add', views.add_property, name='add_property'),
    path('property/<int:property_id>', views.property, name='property'),
    path('edit/<int:property_id>', views.edit, name='edit'),
    path('search', views.search, name='search'), 
] 