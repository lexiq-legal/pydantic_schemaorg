from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class RadioSeries(CreativeWorkSeries):
    """CreativeWorkSeries dedicated to radio broadcast and associated online delivery.

    See: https://schema.org/RadioSeries
    Model depth: 4
    """
    type_: str = Field("RadioSeries", alias='@type')
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
    seasons: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        None,
        description="A season in a media series.",
    )
    season: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWorkSeason', str]], AnyUrl, 'URL', 'CreativeWorkSeason', str]] = Field(
        None,
        description="A season in a media series.",
    )
    actor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
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
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Episode import Episode
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.MusicGroup import MusicGroup
