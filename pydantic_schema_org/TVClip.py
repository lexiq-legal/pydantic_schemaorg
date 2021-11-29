from pydantic import Field
from pydantic_schema_org.TVSeries import TVSeries
from typing import Any, Optional, Union, List
from pydantic_schema_org.Clip import Clip


class TVClip(Clip):
    """A short TV program or a segment/part of a TV program.

    See https://schema.org/TVClip.

    """

    partOfTVSeries: Optional[Union[List[TVSeries], TVSeries]] = Field(
        None,
        description="The TV series to which this episode or season belongs.",
    )
    locals().update({"@type": Field("TVClip", const=True)})


TVClip.update_forward_refs()
