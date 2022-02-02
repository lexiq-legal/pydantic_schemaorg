from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class CreativeWorkSeason(CreativeWork):
    """A media season e.g. tv, radio, video game etc.

    See: https://schema.org/CreativeWorkSeason
    Model depth: 3
    """
    type_: str = Field("CreativeWorkSeason", alias='@type')
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
    endDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
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
    seasonNumber: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        None,
        description="Position of the season within an ordered group of seasons.",
    )
    startDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    episode: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        None,
        description="An episode of a tv, radio or game media within a series or season.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Episode import Episode
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries
    from pydantic_schemaorg.Text import Text
