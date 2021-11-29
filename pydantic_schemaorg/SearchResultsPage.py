from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class SearchResultsPage(WebPage):
    """Web page type: Search results page.

    See https://schema.org/SearchResultsPage.

    """

    locals().update({"@type": Field("SearchResultsPage", const=True)})


SearchResultsPage.update_forward_refs()
