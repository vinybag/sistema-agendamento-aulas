from django.urls import path
from . import views

urlpatterns = [
    path('agendar/', views.agendar, name='agendar'),
    path(
        'confirmacao/<int:agendamento_id>/',
        views.confirmacao,
        name='confirmacao'
    ),
]
