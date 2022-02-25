from django.core.mail import send_mail
from send_email.celery import app

from .service import send
from .models import Contact


@app.task
def send_span_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на наш сервис уведомлений',
            "Мы будем присылать много спама каждый 5 минут ",
            'it.coder@gamil.com',
            [contact.email],
            fail_silently=False
        )
