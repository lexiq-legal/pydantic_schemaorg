from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class WatchAction(ConsumeAction):
    """The act of consuming dynamic/moving visual content.

    See: https://schema.org/WatchAction
    Model depth: 4
    """
    type_: str = Field("WatchAction", alias='@type')
    

