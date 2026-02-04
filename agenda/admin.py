from django.contrib import admin
from .models import Agendamento, Aula

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = (
        'nome_responsavel',
        'nome_aluna',
        'idade_aluna',
        'data',
        'horario',
    )


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dia_semana', 'horario', 'ativa')
    list_filter = ('dia_semana', 'ativa')
    list_editable = ('ativa',)
