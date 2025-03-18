from _user.constants import VERIFY_EMAIL_TOKEN_EXPIRE
from common.helpers.jwt import JwtHelper
from db.models import User


def generate_email_verify_token(user: User) -> str:
    jwt_helper = JwtHelper()

    sub = {
        'user_id': user.id,  # type:ignore
        'email': user.email,
    }

    return jwt_helper.encode(payload=sub, exp=VERIFY_EMAIL_TOKEN_EXPIRE)


def verify_email_verify_token(token: str) -> bool | None:
    jwt_helper = JwtHelper()

    try:
        sub = jwt_helper.decode(token)
    except Exception as exc:
        print(f'JWT error: {exc}')
        return False

    user_id = sub.get('user_id')
    email = sub.get('email')

    user = User.objects.filter(id=user_id).first()
    if user and user.email == email:
        user.is_email_verified = True
        user.save()
        return True
