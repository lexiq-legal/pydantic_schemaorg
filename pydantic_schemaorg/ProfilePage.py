from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class ProfilePage(WebPage):
    """Web page type: Profile page.

    See: https://schema.org/ProfilePage
    Model depth: 4
    """
    type_: str = Field("ProfilePage", alias='@type')
    

