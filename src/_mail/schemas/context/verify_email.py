import os
from typing import NamedTuple


class VerifyEmailContextSchema(NamedTuple):
    email: str
    token: str
    url: str = os.getenv('VERIFY_EMAIL_URL', '')
