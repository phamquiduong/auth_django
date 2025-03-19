from typing import Literal

from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError

from _user.constants.verify_email import VERIFY_EMAIL_TOKEN_EXPIRE
from common.helpers.jwt import JwtHelper
from db.models import User


def generate_email_verify_token(user: User) -> str:
    jwt_helper = JwtHelper()

    sub = {
        'user_id': user.id,  # type:ignore
        'email': user.email,
    }

    return jwt_helper.encode(payload=sub, exp=VERIFY_EMAIL_TOKEN_EXPIRE)


def verify_email_verify_token(token: str) -> Literal[True] | str:
    jwt_helper = JwtHelper()

    try:
        payload = jwt_helper.decode(token)
    except ExpiredSignatureError as exp_exc:
        return str(exp_exc)
    except InvalidSignatureError as invalid_exc:
        return str(invalid_exc)

    user_id = payload.get('user_id')
    email = payload.get('email')

    try:
        user = User.objects.get(id=user_id)
        if user.email == email:
            user.is_email_verified = True
            user.save()
            return True
        else:
            return 'User email was changed'
    except User.DoesNotExist:
        return 'User does not exist'
