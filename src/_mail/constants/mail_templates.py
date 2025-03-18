from enum import Enum

from _mail.schemas.mail_template import MailTemplateSchema


class MailTemplates(Enum):
    VERIFY_EMAIL = MailTemplateSchema(subject='Verify your email', template_name='mail/verify_email.html')
