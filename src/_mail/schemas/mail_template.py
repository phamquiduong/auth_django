from typing import NamedTuple


class MailTemplateSchema(NamedTuple):
    subject: str
    template_name: str
