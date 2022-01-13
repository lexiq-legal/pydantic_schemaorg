from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WebPage import WebPage


class ContactPage(WebPage):
    """Web page type: Contact page.

    See: https://schema.org/ContactPage
    Model depth: 4
    """

    type_: str = Field("ContactPage", const=True, alias="@type")


if TYPE_CHECKING:

    ContactPage.update_forward_refs()
