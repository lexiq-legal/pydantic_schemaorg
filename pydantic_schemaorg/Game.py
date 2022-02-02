from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Game(CreativeWork):
    """The Game type represents things which are games. These are typically rule-governed"
     "recreational activities, e.g. role-playing games in which players assume the role"
     "of characters in a fictional setting.

    See: https://schema.org/Game
    Model depth: 3
    """
    type_: str = Field("Game", alias='@type')
    gameLocation: Optional[Union[List[Union[AnyUrl, 'URL', 'Place', 'PostalAddress', str]], AnyUrl, 'URL', 'Place', 'PostalAddress', str]] = Field(
        None,
        description="Real or fictional location of the game (or part of game).",
    )
    characterAttribute: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="A piece of data that represents a particular aspect of a fictional character (skill,"
     "power, character points, advantage, disadvantage).",
    )
    quest: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="The task that a player-controlled character, or group of characters may complete in"
     "order to gain a reward.",
    )
    gameItem: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="An item is an object within the game world that can be collected by a player or, occasionally,"
     "a non-player character.",
    )
    numberOfPlayers: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="Indicate how many people can play this game (minimum, maximum, or range).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
