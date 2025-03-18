from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_GET, require_POST

from _mail.constants.mail_templates import VERIFY_EMAIL_TEMPLATE
from _mail.schemas import VerifyEmailContextSchema
from _mail.services import SendMailService
from _user.utils.email_verify_token import generate_email_verify_token, verify_email_verify_token


@require_POST
def send_verify_email_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_email_verified:  # type:ignore
        messages.warning(request, 'The email is already verified')
        return redirect('user-profile')

    mail_service = SendMailService(mail_template=VERIFY_EMAIL_TEMPLATE)

    context = VerifyEmailContextSchema(
        email=request.user.email,  # type:ignore
        token=generate_email_verify_token(user=request.user),  # type:ignore
    )._asdict()

    if mail_service.send(context=context, to=request.user.email):  # type:ignore
        messages.success(request, 'Verification email sent. Please check your email inbox.')
    else:
        messages.error(request, 'Failed to send verification email.')

    return redirect('user-profile')


@require_GET
def verify_email_view(request: HttpRequest) -> HttpResponse:
    token = request.GET.get('token', '')

    if verify_email_verify_token(token=token) is True:
        messages.success(request, 'Email verified successfully.')
    else:
        messages.error(request, 'Invalid or expired token.')

    return redirect('home')
