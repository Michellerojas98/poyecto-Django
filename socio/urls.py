from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarMisperris/', views.registrarMisperris),
    path('edicionMisperris/<nombre>', views.edicionMisperris),
    path('editarMisperris/', views.editarMisperris),
    path('eliminarMisperris/<nombre>', views.eliminarMisperris)
]