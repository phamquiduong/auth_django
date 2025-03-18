from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.utils import timezone


class JwtHelper:
    def __init__(
        self,
        secret_key: str = settings.SECRET_KEY,
        algorithm: str = 'HS256'
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def encode(
        self, payload: dict,
        exp: datetime | timedelta | None = None,
        nbf: datetime | timedelta | None = None,
    ) -> str:
        now = timezone.now()
        payload['iat'] = now

        if isinstance(exp, timedelta):
            exp = now + exp
        if exp:
            payload['exp'] = exp

        if isinstance(nbf, timedelta):
            nbf = now + nbf
        if nbf:
            payload['nbf'] = nbf

        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode(self, token: str) -> dict:
        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
