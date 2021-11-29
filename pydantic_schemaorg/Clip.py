from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Person import Person
from decimal import Decimal
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries
from pydantic_schemaorg.CreativeWork import CreativeWork


class Clip(CreativeWork):
    """A short TV or radio program or a segment/part of a program.

    See https://schema.org/Clip.

    """

    partOfSeason: Any = Field(
        None,
        description="The season to which this episode belongs.",
    )
    actors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    director: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    startOffset: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
     "work.",
    )
    clipNumber: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="Position of the clip within an ordered group of clips.",
    )
    partOfSeries: Optional[Union[List[CreativeWorkSeries], CreativeWorkSeries]] = Field(
        None,
        description="The series to which this episode or season belongs.",
    )
    actor: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    partOfEpisode: Any = Field(
        None,
        description="The episode to which this clip belongs.",
    )
    endOffset: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The end time of the clip expressed as the number of seconds from the beginning of the work.",
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
    locals().update({"@type": Field("Clip", const=True)})


Clip.update_forward_refs()
