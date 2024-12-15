import smtplib
import ssl
import smtplib
from template.email import *
from utils.Customer import Customer,Type

def build_email_message(customer: Customer):
    message = MessageBuilder().set_reciever(customer.email)
    if(customer.type == Type.PREVENT):
         message.set_subject(SUBJECT_CUSTOMER).set_body(BODY_CUSTOMER(customer.books))
    else:
        message.set_subject(SUBJECT_BOSS).set_body(BODY_BOSS(customer,customer.books))         
    return message.build() 


def send_email(customer: Customer):
    message=build_email_message(customer)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(EMAIL_SENDER,EMAIL_PASSWORD)
            errors = smtp.sendmail(EMAIL_SENDER,message["To"],message.as_string())
    return errors