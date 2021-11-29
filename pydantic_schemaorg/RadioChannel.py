from pydantic import Field
from pydantic_schemaorg.BroadcastChannel import BroadcastChannel


class RadioChannel(BroadcastChannel):
    """A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.

    See https://schema.org/RadioChannel.

    """

    locals().update({"@type": Field("RadioChannel", const=True)})


RadioChannel.update_forward_refs()
