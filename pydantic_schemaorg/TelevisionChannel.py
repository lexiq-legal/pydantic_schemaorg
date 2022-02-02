from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BroadcastChannel import BroadcastChannel


class TelevisionChannel(BroadcastChannel):
    """A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.

    See: https://schema.org/TelevisionChannel
    Model depth: 4
    """
    type_: str = Field("TelevisionChannel", alias='@type')
    

