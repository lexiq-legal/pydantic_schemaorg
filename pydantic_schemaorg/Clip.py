from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Clip(CreativeWork):
    """A short TV or radio program or a segment/part of a program.

    See: https://schema.org/Clip
    Model depth: 3
    """
    type_: str = Field("Clip", alias='@type')
    partOfSeason: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        None,
        description="The season to which this episode belongs.",
    )
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    director: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    startOffset: Optional[Union[List[Union[Decimal, 'Number', 'HyperTocEntry', str]], Decimal, 'Number', 'HyperTocEntry', str]] = Field(
        None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
     "work.",
    )
    clipNumber: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        None,
        description="Position of the clip within an ordered group of clips.",
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
    partOfEpisode: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        None,
        description="The episode to which this clip belongs.",
    )
    endOffset: Optional[Union[List[Union[Decimal, 'Number', 'HyperTocEntry', str]], Decimal, 'Number', 'HyperTocEntry', str]] = Field(
        None,
        description="The end time of the clip expressed as the number of seconds from the beginning of the work.",
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
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries
    from pydantic_schemaorg.Episode import Episode
    from pydantic_schemaorg.MusicGroup import MusicGroup
