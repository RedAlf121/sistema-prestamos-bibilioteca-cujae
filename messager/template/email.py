from email.message import EmailMessage

EMAIL_SENDER='cujaebiblioteca@gmail.com'
EMAIL_PASSWORD='olzdjmbxiptezrgj'

SUBJECT_CUSTOMER='Mensaje de aviso'

BODY_CUSTOMER=lambda books: f"Debes {len(books)}, {books}"

SUBJECT_BOSS='Mensaje de aviso(Comisión disciplinaria)'

BODY_BOSS=lambda customer,books: f"El {customer.category} {customer.name} debe {len(books)}, {books}"


class MessageBuilder:
    def __init__(self):
        self.email_message = EmailMessage()
        self.email_message["From"]=EMAIL_SENDER
    def set_reciever(self,reciever):
        self.email_message["To"]=reciever
        return self
    def set_subject(self,subject):
        self.email_message["Subject"]=subject
        return self
    def set_body(self,body):
        self.email_message.set_content(body)
        return self
    def build(self):
        response = self.email_message
        self.email_message = EmailMessage()
        self.email_message["From"]=EMAIL_SENDER
        return response