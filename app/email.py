from flask_mail import Message
from flask import render_template
from . import mail

def welcome_message(subject,template,to,**kwargs):
    sender_email = "kilewa@gmail.com"-to chnge-

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)

def notification_message(subject,template,to,**kwargs):
    sender_email = "kilewa@gmail.com"

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)