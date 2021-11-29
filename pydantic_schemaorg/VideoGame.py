from pydantic import Field, AnyUrl
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.GamePlayMode import GamePlayMode
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.SoftwareApplication import SoftwareApplication
from pydantic_schemaorg.Game import Game


class VideoGame(SoftwareApplication, Game):
    """A video game is an electronic game that involves human interaction with a user interface"
     "to generate visual feedback on a video device.

    See https://schema.org/VideoGame.

    """

    actors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    trailer: Any = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
    )
    director: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    gamePlatform: Optional[Union[List[Union[AnyUrl, str, Thing]], Union[AnyUrl, str, Thing]]] = Field(
        None,
        description="The electronic systems used to play <a href=\"http://en.wikipedia.org/wiki/Category:Video_game_platforms\">video"
     "games</a>.",
    )
    playMode: Optional[Union[List[GamePlayMode], GamePlayMode]] = Field(
        None,
        description="Indicates whether this game is multi-player, co-op or single-player. The game can be"
     "marked as multi-player, co-op and single-player at the same time.",
    )
    cheatCode: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="Cheat codes to the game.",
    )
    actor: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    gameTip: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="Links to tips, tactics, etc.",
    )
    gameServer: Any = Field(
        None,
        description="The server on which it is possible to play the game.",
    )
    directors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    musicBy: Union[List[Union[Person, Any]], Union[Person, Any]] = Field(
        None,
        description="The composer of the soundtrack.",
    )
    locals().update({"@type": Field("VideoGame", const=True)})


VideoGame.update_forward_refs()
