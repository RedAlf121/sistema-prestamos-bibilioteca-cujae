import ssl
import smtplib
from messager.email import EMAIL_PASSWORD, EMAIL_SENDER, factory
from messager.email.models import Customer, Type

def send(customer: Customer=None, type: Type=Type.PREVENT):
    message=factory.build_email_message(customer,type)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(EMAIL_SENDER,EMAIL_PASSWORD)
            errors = smtp.sendmail(EMAIL_SENDER, message["To"], message.as_string()) 
    return errors


