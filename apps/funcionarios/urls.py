from django.urls import path, include
from .views import funcionario
urlpatterns = [
    path('', funcionario ),
]