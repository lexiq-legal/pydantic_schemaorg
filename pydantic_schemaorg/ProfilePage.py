from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WebPage import WebPage


class ProfilePage(WebPage):
    """Web page type: Profile page.

    See: https://schema.org/ProfilePage
    Model depth: 4
    """

    type_: str = Field("ProfilePage", const=True, alias="@type")


if TYPE_CHECKING:

    ProfilePage.update_forward_refs()
