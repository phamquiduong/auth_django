from django.conf import settings

from _mail.schemas.mail_template import MailTemplateSchema

VERIFY_EMAIL_TEMPLATE = MailTemplateSchema(
    subject=f'[{settings.PROJECT_NAME}] Verify your email',
    template_name='mail/verify_email.html'
)
