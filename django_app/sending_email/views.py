from django.core.mail import send_mail
from django.shortcuts import render, redirect


def index(request):
    # send_mail(
    #     '테스트입니다',
    #     '안녕?',
    #     'kizmo04@gmail.com',
    #     ['30sexytori@gmail.com'],
    #     fail_silently=True,
    # )
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        if subject and message and from_email:

        return redirect()
    else:
        context = {

        }
    return render(request, 'common/index.html', context)
