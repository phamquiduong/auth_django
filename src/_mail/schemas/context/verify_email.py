import os
from typing import NamedTuple

from django.conf import settings


class VerifyEmailContextSchema(NamedTuple):
    email: str
    token: str
    url: str = os.getenv('VERIFY_EMAIL_URL', '')
    project_name: str = settings.PROJECT_NAME
