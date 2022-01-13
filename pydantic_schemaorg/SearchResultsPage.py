from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WebPage import WebPage


class SearchResultsPage(WebPage):
    """Web page type: Search results page.

    See: https://schema.org/SearchResultsPage
    Model depth: 4
    """

    type_: str = Field("SearchResultsPage", const=True, alias="@type")


if TYPE_CHECKING:

    SearchResultsPage.update_forward_refs()
