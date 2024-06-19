from pydantic import EmailStr
from .celery import celery
from .email_templates import create_email_for_verification
import smtplib
from core import settings


@celery.task
def send_email_for_verification_task(email_to: EmailStr = ''):
    email = 'serj2626@mail.ru'
    mail_content = create_email_for_verification(email)

    with smtplib.SMTP_SSL(host=settings.SMTP_HOST, port=settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(mail_content)
    return f'Task Done! Письмо отправлено на почту {email_to}'
