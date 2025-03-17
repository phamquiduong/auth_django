import os
import uuid


def normalize_email(email: str) -> str:
    email = email.lower().strip()
    local_part, domain = email.split('@')

    if domain in ('gmail.com', 'googlemail.com'):
        local_part = local_part.split('+')[0]
        local_part = local_part.replace('.', '')
        domain = 'gmail.com'

    return f'{local_part}@{domain}'


def avatar_image_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('avatar/', new_filename)
