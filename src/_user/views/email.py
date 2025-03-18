from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.decorators.http import require_GET, require_POST

from _mail.constants.mail_templates import MailTemplates
from _mail.schemas.context.verify_email import VerifyEmailContextSchema
from _mail.services import SendMailService
from _user.utils.email_verify_token import generate_email_verify_token, verify_email_verify_token


@require_POST
def send_verify_email_view(request: HttpRequest):
    if request.user.is_email_verified:
        messages.warning(request, 'The email is already verified')
        return redirect('user-profile')

    mail_service = SendMailService(mail_template=MailTemplates.VERIFY_EMAIL.value)

    context = VerifyEmailContextSchema(
        email=request.user.email,
        token=generate_email_verify_token(user=request.user),
    )._asdict()

    if mail_service.send(context=context, to=request.user.email):
        messages.success(request, 'Verification email sent. Please check your email inbox.')
    else:
        messages.error(request, 'Failed to send verification email.')

    return redirect('user-profile')


@require_GET
def verify_email_view(request: HttpRequest):
    token = request.GET.get('token', '')

    if verify_email_verify_token(token=token):
        messages.success(request, 'Email verified successfully.')
    else:
        messages.error(request, 'Invalid or expired token.')

    return redirect('home')
