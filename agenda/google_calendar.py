from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings
from datetime import datetime, timedelta
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar']


def criar_evento_google(agendamento):
    credentials = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_CALENDAR_CREDENTIALS,
        scopes=SCOPES
    )

    service = build('calendar', 'v3', credentials=credentials)

    fuso = pytz.timezone('America/Sao_Paulo')

    inicio = fuso.localize(
        datetime.combine(agendamento.data, agendamento.horario)
    )

    fim = inicio + timedelta(hours=1)

    evento = {
        'summary': f"Aula experimental – {agendamento.nome_aluna}",
        'description': (
            f"Responsável: {agendamento.nome_responsavel}\n"
            f"Aula: {agendamento.aula.nome}\n"
            f"Telefone: {agendamento.telefone}\n"
            f"E-mail: {agendamento.email}"
        ),
        'start': {
            'dateTime': inicio.isoformat(),
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': fim.isoformat(),
            'timeZone': 'America/Sao_Paulo',
        },
    }

    service.events().insert(
        calendarId=settings.GOOGLE_CALENDAR_ID,
        body=evento
    ).execute()

