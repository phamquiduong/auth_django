from datetime import timedelta
from enum import StrEnum

DEFAULT_FULL_NAME = 'Uknown'


class Role(StrEnum):
    ADMIN = 'admin'
    GUEST = 'guest'


VERIFY_EMAIL_TOKEN_EXPIRE = timedelta(minutes=5)
