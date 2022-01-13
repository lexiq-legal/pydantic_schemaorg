from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Organization import Organization


class SportsOrganization(Organization):
    """Represents the collection of all sports organizations, including sports teams, governing"
     "bodies, and sports associations.

    See: https://schema.org/SportsOrganization
    Model depth: 3
    """

    type_: str = Field("SportsOrganization", const=True, alias="@type")
    sport: "Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]]" = Field(
        None,
        description="A type of sport (e.g. Baseball).",
    )


if TYPE_CHECKING:

    from pydantic import AnyUrl

    SportsOrganization.update_forward_refs()
