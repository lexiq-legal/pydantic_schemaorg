from pydantic import Field
from pydantic_schemaorg.BroadcastChannel import BroadcastChannel


class TelevisionChannel(BroadcastChannel):
    """A unique instance of a television BroadcastService on a CableOrSatelliteService lineup.

    See https://schema.org/TelevisionChannel.

    """

    locals().update({"@type": Field("TelevisionChannel", const=True)})


TelevisionChannel.update_forward_refs()
