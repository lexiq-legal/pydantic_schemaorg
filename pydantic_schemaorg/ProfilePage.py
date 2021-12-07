from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class ProfilePage(WebPage):
    """Web page type: Profile page.

    See https://schema.org/ProfilePage.

    """
    type_: str = Field("ProfilePage", const=True, alias='@type')
    

ProfilePage.update_forward_refs()
