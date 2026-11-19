from django.urls import path
from . import views

urlpatterns = [
    path('programas/crear/', views.programa_crear, name='programa_crear'),
]
