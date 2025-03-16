from typing import Any

from django.template.defaulttags import register

from common.constants.get_item import GET_ITEM_TAG_DEFAULT


@register.filter
def get_item(dictionary: dict | None, key: str) -> Any:
    return dictionary.get(key, GET_ITEM_TAG_DEFAULT) if dictionary else GET_ITEM_TAG_DEFAULT
