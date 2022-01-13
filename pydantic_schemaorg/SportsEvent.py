from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Event import Event


class SportsEvent(Event):
    """Event type: Sports event.

    See: https://schema.org/SportsEvent
    Model depth: 3
    """

    type_: str = Field("SportsEvent", const=True, alias="@type")
    sport: "Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]]" = Field(
        None,
        description="A type of sport (e.g. Baseball).",
    )
    awayTeam: "Optional[Union[List[Union[SportsTeam, Person, str]], Union[SportsTeam, Person, str]]]" = Field(
        None,
        description="The away team in a sports event.",
    )
    homeTeam: "Optional[Union[List[Union[SportsTeam, Person, str]], Union[SportsTeam, Person, str]]]" = Field(
        None,
        description="The home team in a sports event.",
    )
    competitor: "Optional[Union[List[Union[SportsTeam, Person, str]], Union[SportsTeam, Person, str]]]" = Field(
        None,
        description="A competitor in a sports event.",
    )


if TYPE_CHECKING:

    from pydantic import AnyUrl

    from pydantic_schemaorg.SportsTeam import SportsTeam

    from pydantic_schemaorg.Person import Person

    SportsEvent.update_forward_refs()
