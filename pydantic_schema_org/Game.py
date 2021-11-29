from pydantic import AnyUrl, Field
from pydantic_schema_org.PostalAddress import PostalAddress
from pydantic_schema_org.Place import Place
from typing import Any, Optional, Union, List
from pydantic_schema_org.Thing import Thing
from pydantic_schema_org.QuantitativeValue import QuantitativeValue
from pydantic_schema_org.CreativeWork import CreativeWork


class Game(CreativeWork):
    """The Game type represents things which are games. These are typically rule-governed"
     "recreational activities, e.g. role-playing games in which players assume the role"
     "of characters in a fictional setting.

    See https://schema.org/Game.

    """

    gameLocation: Optional[Union[List[Union[AnyUrl, PostalAddress, Place]], Union[AnyUrl, PostalAddress, Place]]] = Field(
        None,
        description="Real or fictional location of the game (or part of game).",
    )
    characterAttribute: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="A piece of data that represents a particular aspect of a fictional character (skill,"
     "power, character points, advantage, disadvantage).",
    )
    quest: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The task that a player-controlled character, or group of characters may complete in"
     "order to gain a reward.",
    )
    gameItem: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="An item is an object within the game world that can be collected by a player or, occasionally,"
     "a non-player character.",
    )
    numberOfPlayers: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="Indicate how many people can play this game (minimum, maximum, or range).",
    )
    locals().update({"@type": Field("Game", const=True)})


Game.update_forward_refs()
