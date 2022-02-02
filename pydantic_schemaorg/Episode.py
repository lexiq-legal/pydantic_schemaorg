from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Episode(CreativeWork):
    """A media episode (e.g. TV, radio, video game) which can be part of a series or season.

    See: https://schema.org/Episode
    Model depth: 3
    """
    type_: str = Field("Episode", alias='@type')
    partOfSeason: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        None,
        description="The season to which this episode belongs.",
    )
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    episodeNumber: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        None,
        description="Position of the episode within an ordered group of episodes.",
    )
    trailer: Optional[Union[List[Union['VideoObject', str]], 'VideoObject', str]] = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
    )
    duration: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
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
    partOfSeries: Optional[Union[List[Union['CreativeWorkSeries', str]], 'CreativeWorkSeries', str]] = Field(
        None,
        description="The series to which this episode or season belongs.",
    )
    actor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
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
    from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries
    from pydantic_schemaorg.MusicGroup import MusicGroup
