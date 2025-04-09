from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from jinja2 import Environment, FileSystemLoader
from messager.email import EMAIL_SENDER
from enum import Enum,auto

class Type(Enum):
    IMPORTANT = auto()
    PREVENT = auto()

class Category(Enum):
    STUDENT = auto()
    TEACHER = auto()

@dataclass
class Customer:
    name: str
    email: str
    books:list
    category: Category

@dataclass
class Boss:
    name: str
    email: str
    customer: Customer

@dataclass
class Template:
    template: str
    subject: str
    data: dir

class EmailMessager:
    def __init__(self,reciever,template,subject,args:dict={}):
        self.email_message = MIMEMultipart()
        self.email_message["From"]=EMAIL_SENDER
        self.email_message["To"]=reciever
        self.email_message["Subject"]=subject
        templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
        environment = Environment(loader=FileSystemLoader(templates_dir))
        html_content = environment.get_template(template).render(args)
        self.email_message.attach(MIMEText(html_content, 'html'))
    def get_email_message(self):
        return self.email_message
