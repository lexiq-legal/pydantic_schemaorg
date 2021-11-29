from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class AboutPage(WebPage):
    """Web page type: About page.

    See https://schema.org/AboutPage.

    """

    locals().update({"@type": Field("AboutPage", const=True)})


AboutPage.update_forward_refs()
