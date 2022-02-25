from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на наш сервис уведомлений',
        "Мы будем присылать много спама",
        'it.coder@gamil.com',
        [user_email],
        fail_silently=False
    )
