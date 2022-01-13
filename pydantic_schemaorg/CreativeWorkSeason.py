from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class CreativeWorkSeason(CreativeWork):
    """A media season e.g. tv, radio, video game etc.

    See: https://schema.org/CreativeWorkSeason
    Model depth: 3
    """

    type_: str = Field("CreativeWorkSeason", const=True, alias="@type")
    trailer: "Optional[Union[List[Union[VideoObject, str]], Union[VideoObject, str]]]" = Field(
        None,
        description="The trailer of a movie or tv/radio series, season, episode, etc.",
    )
    episodes: "Optional[Union[List[Union[Episode, str]], Union[Episode, str]]]" = Field(
        None,
        description="An episode of a TV/radio series or season.",
    )
    numberOfEpisodes: "Optional[Union[List[Union[int, str]], Union[int, str]]]" = Field(
        None,
        description="The number of episodes in this season or series.",
    )
    director: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
        "can be associated with individual items or with a series, episode, clip.",
    )
    productionCompany: "Optional[Union[List[Union[Organization, str]], Union[Organization, str]]]" = Field(
        None,
        description="The production company or studio responsible for the item e.g. series, video game, episode"
        "etc.",
    )
    endDate: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    partOfSeries: "Optional[Union[List[Union[CreativeWorkSeries, str]], Union[CreativeWorkSeries, str]]]" = Field(
        None,
        description="The series to which this episode or season belongs.",
    )
    actor: "Optional[Union[List[Union[Person, str]], Union[Person, str]]]" = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
        "with individual items or with a series, episode, clip.",
    )
    seasonNumber: "Optional[Union[List[Union[int, str]], Union[int, str]]]" = Field(
        None,
        description="Position of the season within an ordered group of seasons.",
    )
    startDate: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    episode: "Optional[Union[List[Union[Episode, str]], Union[Episode, str]]]" = Field(
        None,
        description="An episode of a tv, radio or game media within a series or season.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.VideoObject import VideoObject

    from pydantic_schemaorg.Episode import Episode

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    from datetime import date, datetime

    from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries

    CreativeWorkSeason.update_forward_refs()
