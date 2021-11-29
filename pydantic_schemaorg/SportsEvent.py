from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.SportsTeam import SportsTeam
from pydantic_schemaorg.Event import Event


class SportsEvent(Event):
    """Event type: Sports event.

    See https://schema.org/SportsEvent.

    """

    sport: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="A type of sport (e.g. Baseball).",
    )
    awayTeam: Optional[Union[List[Union[Person, SportsTeam]], Union[Person, SportsTeam]]] = Field(
        None,
        description="The away team in a sports event.",
    )
    homeTeam: Optional[Union[List[Union[Person, SportsTeam]], Union[Person, SportsTeam]]] = Field(
        None,
        description="The home team in a sports event.",
    )
    competitor: Optional[Union[List[Union[Person, SportsTeam]], Union[Person, SportsTeam]]] = Field(
        None,
        description="A competitor in a sports event.",
    )
    locals().update({"@type": Field("SportsEvent", const=True)})


SportsEvent.update_forward_refs()
