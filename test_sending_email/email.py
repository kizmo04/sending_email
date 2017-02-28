from django.core.mail import send_mail

send_mail(
    '테스트입니다',
    '안녕?',
    'kizmo04@gmail.com',
    ['kizmo04@daum.net'],
    fail_silently=True,
)
