from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from _mail.constants.mail_services import MailServices
from _mail.schemas.context.verify_email import VerifyEmailContextSchema


@require_POST
def email_view(request: HttpRequest):
    mail_service = MailServices.VERIFY_EMAIL.value

    context = VerifyEmailContextSchema(
        email=request.user.email,  # type: ignore
        token='abc',
    )._asdict()

    if mail_service.send(context=context, to=request.user.email):   # type: ignore
        messages.success(request, 'Verification email sent. Please check your email inbox.')
    else:
        messages.error(request, 'Failed to send verification email.')

    return redirect('user-profile')
