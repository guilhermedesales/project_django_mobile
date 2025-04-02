from django.urls import path
from .views import login_view

urlpatterns = [
    path('', login_view, name="index"),  # URL da tela de login
]
