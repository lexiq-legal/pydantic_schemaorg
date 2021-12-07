from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class SearchResultsPage(WebPage):
    """Web page type: Search results page.

    See https://schema.org/SearchResultsPage.

    """
    type_: str = Field("SearchResultsPage", const=True, alias='@type')
    

SearchResultsPage.update_forward_refs()
