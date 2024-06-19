from logging import config

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from core import settings
from tasks.celery import celery

conf = ConnectionConfig(
    MAIL_USERNAME="Serj",
    MAIL_PASSWORD=settings.SMTP_PASS,
    MAIL_FROM=settings.SMTP_USER,
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_SERVER=settings.SMTP_HOST,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)

#     "MAIL_USERNAME": "Serj",
#     "MAIL_PASSWORD": settings.SMTP_PASS,
#     "MAIL_FROM": settings.SMTP_USER,
#     "MAIL_PORT": settings.SMTP_PORT,
#     "MAIL_SERVER": settings.SMTP_HOST,
#     MAIL_STARTTLS = True,
#     MAIL_SSL_TLS = False,
# }


@celery.task
def send_email_verification(username: str, email: str):
    template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Письмо подтверждения</title>
        </head>
        <body>
        <div style="display: flex; flex-direction: column; align-items: center;">
            <h1>Подвтердите свою почту</h1>
            <p>
                Привет {username}, спасибо что выбрали наш сервис,
                кликните на ссылку ниже для подтверждения своей почты
            </p>
            <a
                style="text-decoration: none;
                margin-top: 10px;
                margin-bottom: 10px;
                padding: 10px;
                border-radius: 5px;
                background-color: blue;
                color: white;"
                href="http://127.0.0.1:8000/api/users/verify/{email}">
                Подтвердить почту
            </a>
            <hr>
            <p>С уважением, команда нашего сервиса</p>
        </div>

        </body>
        </html>
    """
    message = MessageSchema(
        subject="Подтверждение почты",
        recipients=[email],
        body=template,
        subtype=MessageType.html,
    )

    fm = FastMail(conf)
    fm.send_message(message)
    return f"Send verification email to {username} with {email}"
