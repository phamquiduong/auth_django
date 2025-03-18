import os
import uuid


def avatar_image_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('avatar/', new_filename)
