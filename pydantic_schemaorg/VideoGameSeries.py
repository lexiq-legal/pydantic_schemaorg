from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class VideoGameSeries(CreativeWorkSeries):
    """A video game series.

    See: https://schema.org/VideoGameSeries
    Model depth: 4
    """
    type_: str = Field("VideoGameSeries", alias='@type')
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    containsSeason: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        None,
        description="A season that is part of the media series.",
    )
    numberOfSeasons: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="The number of seasons in this series.",
    )
    gameLocation: Optional[Union[List[Union[AnyUrl, 'URL', 'Place', 'PostalAddress', str]], AnyUrl, 'URL', 'Place', 'PostalAddress', str]] = Field(
        None,
        description="Real or fictional location of the game (or part of game).",
    )
    trailer: Optional[Union[List[Union['VideoObject', str]], 'VideoObject', str]] = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
    )
    episodes: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        None,
        description="An episode of a TV/radio series or season.",
    )
    numberOfEpisodes: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="The number of episodes in this season or series.",
    )
    director: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    productionCompany: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The production company or studio responsible for the item e.g. series, video game, episode"
     "etc.",
    )
    gamePlatform: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing']], AnyUrl, 'URL', str, 'Text', 'Thing']] = Field(
        None,
        description="The electronic systems used to play <a href=\"http://en.wikipedia.org/wiki/Category:Video_game_platforms\">video"
     "games</a>.",
    )
    seasons: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        None,
        description="A season in a media series.",
    )
    season: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWorkSeason', str]], AnyUrl, 'URL', 'CreativeWorkSeason', str]] = Field(
        None,
        description="A season in a media series.",
    )
    playMode: Optional[Union[List[Union['GamePlayMode', str]], 'GamePlayMode', str]] = Field(
        None,
        description="Indicates whether this game is multi-player, co-op or single-player. The game can be"
     "marked as multi-player, co-op and single-player at the same time.",
    )
    characterAttribute: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="A piece of data that represents a particular aspect of a fictional character (skill,"
     "power, character points, advantage, disadvantage).",
    )
    cheatCode: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="Cheat codes to the game.",
    )
    actor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
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
    episode: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        None,
        description="An episode of a tv, radio or game media within a series or season.",
    )
    directors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    musicBy: Optional[Union[List[Union['MusicGroup', 'Person', str]], 'MusicGroup', 'Person', str]] = Field(
        None,
        description="The composer of the soundtrack.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Episode import Episode
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.GamePlayMode import GamePlayMode
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.MusicGroup import MusicGroup
