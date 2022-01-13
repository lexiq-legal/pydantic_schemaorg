from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Clip import Clip


class TVClip(Clip):
    """A short TV program or a segment/part of a TV program.

    See: https://schema.org/TVClip
    Model depth: 4
    """

    type_: str = Field("TVClip", const=True, alias="@type")
    partOfTVSeries: "Optional[Union[List[Union[TVSeries, str]], Union[TVSeries, str]]]" = Field(
        None,
        description="The TV series to which this episode or season belongs.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.TVSeries import TVSeries

    TVClip.update_forward_refs()
