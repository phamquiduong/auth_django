from enum import Enum

from _mail.constants.mail_templates import MailTemplates
from _mail.services import SendMailService


class MailServices(Enum):
    VERIFY_EMAIL = SendMailService(mail_template=MailTemplates.VERIFY_EMAIL.value)
