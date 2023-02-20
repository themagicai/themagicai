from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(data):
    subject = 'Smart Email'
    # html_message = render_to_string(
    #     'auth/activate.html', {'url': data['url'], 'firstname': data['firstname'], 'lastname': data['lastname'], 'text': data['text']})
    message = (f'Your code: {data["code"]}')
    # plain_message = strip_tags(message1)
    from_email = settings.EMAIL_HOST_USER
    to = data['to_email']

    # send_mail(subject=data['email_subject'],message=data['email_body'],from_email=EMAIL_HOST_USER,recipient_list=[data['to_email']])
    send_mail(subject=subject, message=message, from_email=from_email,recipient_list=[to])

def send_message(data):
    subject = 'The Magic AI'
    # html_message = render_to_string(
    #     'auth/activate.html', {'url': data['url'], 'firstname': data['firstname'], 'lastname': data['lastname'], 'text': data['text']})
    message = (data["body"])
    # plain_message = strip_tags(message1)
    from_email = settings.EMAIL_HOST_USER
    to = data['to_email']

    # send_mail(subject=data['email_subject'],message=data['email_body'],from_email=EMAIL_HOST_USER,recipient_list=[data['to_email']])
    send_mail(subject=subject, message=message, from_email=from_email,recipient_list=[to])

