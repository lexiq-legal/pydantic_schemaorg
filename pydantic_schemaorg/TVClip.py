from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Clip import Clip


class TVClip(Clip):
    """A short TV program or a segment/part of a TV program.

    See: https://schema.org/TVClip
    Model depth: 4
    """
    type_: str = Field("TVClip", alias='@type')
    partOfTVSeries: Optional[Union[List[Union['TVSeries', str]], 'TVSeries', str]] = Field(
        None,
        description="The TV series to which this episode or season belongs.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.TVSeries import TVSeries
