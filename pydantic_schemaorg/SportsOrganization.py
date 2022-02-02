from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class SportsOrganization(Organization):
    """Represents the collection of all sports organizations, including sports teams, governing"
     "bodies, and sports associations.

    See: https://schema.org/SportsOrganization
    Model depth: 3
    """
    type_: str = Field("SportsOrganization", alias='@type')
    sport: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="A type of sport (e.g. Baseball).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
