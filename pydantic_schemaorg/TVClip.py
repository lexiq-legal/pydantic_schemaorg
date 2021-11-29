from pydantic import Field
from pydantic_schemaorg.TVSeries import TVSeries
from typing import List, Optional, Union, Any
from pydantic_schemaorg.Clip import Clip


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
