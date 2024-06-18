from tasks.celery import celery

@celery.task
def send_email_verification(username: str, email: str):
    print(f"Send verification email to {username} with {email}")