from django.core.mail import send_mail
from django.shortcuts import render


def index(request):
    send_mail(
        '테스트입니다',
        '안녕?',
        'kizmo04@gmail.com',
        ['30sexytori@gmail.com'],
        fail_silently=True,
    )

    return render(request, 'common/index.html')
