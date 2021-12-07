from pydantic import Field
from pydantic_schemaorg.BroadcastChannel import BroadcastChannel


class RadioChannel(BroadcastChannel):
    """A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.

    See https://schema.org/RadioChannel.

    """
    type_: str = Field("RadioChannel", const=True, alias='@type')
    

RadioChannel.update_forward_refs()
