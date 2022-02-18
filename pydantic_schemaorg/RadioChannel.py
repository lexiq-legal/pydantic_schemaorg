from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BroadcastChannel import BroadcastChannel


class RadioChannel(BroadcastChannel):
    """A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.

    See: https://schema.org/RadioChannel
    Model depth: 4
    """
    type_: str = Field(default="RadioChannel", alias='@type', const=True)
    
