from pydantic import Field, AnyUrl
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.GamePlayMode import GamePlayMode
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class VideoGameSeries(CreativeWorkSeries):
    """A video game series.

    See https://schema.org/VideoGameSeries.

    """

    actors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    containsSeason: Any = Field(
        None,
        description="A season that is part of the media series.",
    )
    numberOfSeasons: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of seasons in this series.",
    )
    gameLocation: Union[List[Union[AnyUrl, Place, Any]], Union[AnyUrl, Place, Any]] = Field(
        None,
        description="Real or fictional location of the game (or part of game).",
    )
    trailer: Any = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
    )
    episodes: Any = Field(
        None,
        description="An episode of a TV/radio series or season.",
    )
    numberOfEpisodes: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of episodes in this season or series.",
    )
    director: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    productionCompany: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The production company or studio responsible for the item e.g. series, video game, episode"
     "etc.",
    )
    gamePlatform: Optional[Union[List[Union[AnyUrl, str, Thing]], Union[AnyUrl, str, Thing]]] = Field(
        None,
        description="The electronic systems used to play <a href=\"http://en.wikipedia.org/wiki/Category:Video_game_platforms\">video"
     "games</a>.",
    )
    seasons: Any = Field(
        None,
        description="A season in a media series.",
    )
    season: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A season in a media series.",
    )
    playMode: Optional[Union[List[GamePlayMode], GamePlayMode]] = Field(
        None,
        description="Indicates whether this game is multi-player, co-op or single-player. The game can be"
     "marked as multi-player, co-op and single-player at the same time.",
    )
    characterAttribute: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="A piece of data that represents a particular aspect of a fictional character (skill,"
     "power, character points, advantage, disadvantage).",
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
    numberOfPlayers: Any = Field(
        None,
        description="Indicate how many people can play this game (minimum, maximum, or range).",
    )
    episode: Any = Field(
        None,
        description="An episode of a tv, radio or game media within a series or season.",
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
    locals().update({"@type": Field("VideoGameSeries", const=True)})


VideoGameSeries.update_forward_refs()
