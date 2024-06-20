from email.message import EmailMessage

from pydantic import EmailStr

from core import settings

localhost_url = f"http://{settings.APP_HOST}:{settings.APP_PORT}"


def create_email_for_verification(email_to: EmailStr):
    email = EmailMessage()
    email["To"] = email_to
    email["From"] = settings.SMTP_USER
    email["Subject"] = "Подтверждение почты"
    email.set_content(
        f"""
            <h1>Подтверждение почты</h1>
            <p>Здравствуйте. {email_to}</p><br>
                <p>Для подтверждения почты перейдите по ссылке: 
                <a href="{localhost_url}/api/v1/users/confirm-email/{email_to}">Активировать</a>
                </p>
            <hr>
            <p>С уважением, администрация сайта</p>
        """,
        subtype="html",
    )

    return email
