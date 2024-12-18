from messager.email import SUBJECT_BOSS, SUBJECT_CUSTOMER
from messager.email.models import EmailMessager, Template
from messager.email.models import Customer,Type


TEMPLATES = {
    Type.PREVENT: lambda customer: TemplateFactory.build_customer_template(customer),
    Type.IMPORTANT: lambda customer: TemplateFactory.build_boss_template(customer)
}
def build_email_message(customer: Customer,type:Type):
    template: Template
    template = TEMPLATES[type](customer)
    return EmailMessager(\
        customer.email,\
        template.template,\
        template.subject,\
        template.data).get_email_message()


class TemplateFactory:
    @staticmethod
    def build_customer_template(customer)->Template:
        template='customer_mail.html'
        subject=SUBJECT_CUSTOMER
        data={
            'name': customer.name,
            'books': ['a','b','c']
        }
        return Template(template,subject,data)
    
    @staticmethod
    def build_boss_template(customer)->Template:
        template='customer_mail.html'
        subject=SUBJECT_BOSS
        data={
            'name': customer.name,
            'books': ['a','c']
        }
        return Template(template,subject,data)


