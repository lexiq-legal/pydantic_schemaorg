from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class FAQPage(WebPage):
    """A [[FAQPage]] is a [[WebPage]] presenting one or more \"[Frequently asked questions](https://en.wikipedia.org/wiki/FAQ)\""
     "(see also [[QAPage]]).

    See https://schema.org/FAQPage.

    """
    type_: str = Field("FAQPage", const=True, alias='@type')
    

FAQPage.update_forward_refs()
