from enum import StrEnum

DEFAULT_FULL_NAME = 'Uknown'


class Role(StrEnum):
    ADMIN = 'admin'
    GUEST = 'guest'
