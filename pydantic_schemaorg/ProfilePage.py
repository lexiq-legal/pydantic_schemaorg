from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class ProfilePage(WebPage):
    """Web page type: Profile page.

    See https://schema.org/ProfilePage.

    """

    locals().update({"@type": Field("ProfilePage", const=True)})


ProfilePage.update_forward_refs()
