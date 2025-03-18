from typing import Any

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from _mail.schemas.mail_template import MailTemplateSchema


class SendMailService:
    def __init__(self, mail_template: MailTemplateSchema) -> None:
        self.mail_template = mail_template

    def send(self, context: dict[str, Any] | None, to: list[str] | str) -> bool:
        if isinstance(to, str):
            to = [to]

        html_message = render_to_string(
            template_name=self.mail_template.template_name,
            context=context
        )

        email = EmailMessage(
            subject=self.mail_template.subject,
            body=html_message,
            to=to,
        )
        email.content_subtype = 'html'

        try:
            email.send()
            return True
        except Exception as exc:
            print(f'Send mail error: {exc}')
            return False
