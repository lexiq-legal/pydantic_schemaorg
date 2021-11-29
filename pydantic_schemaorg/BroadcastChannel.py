from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Intangible import Intangible


class BroadcastChannel(Intangible):
    """A unique instance of a BroadcastService on a CableOrSatelliteService lineup.

    See https://schema.org/BroadcastChannel.

    """

    broadcastChannelId: Optional[Union[List[str], str]] = Field(
        None,
        description="The unique address by which the BroadcastService can be identified in a provider lineup."
     "In US, this is typically a number.",
    )
    broadcastFrequency: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The frequency used for over-the-air broadcasts. Numeric values or simple ranges e.g."
     "87-99. In addition a shortcut idiom is supported for frequences of AM and FM radio channels,"
     "e.g. \"87 FM\".",
    )
    genre: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    providesBroadcastService: Any = Field(
        None,
        description="The BroadcastService offered on this channel.",
    )
    broadcastServiceTier: Optional[Union[List[str], str]] = Field(
        None,
        description="The type of service required to have access to the channel (e.g. Standard or Premium).",
    )
    inBroadcastLineup: Any = Field(
        None,
        description="The CableOrSatelliteService offering the channel.",
    )
    locals().update({"@type": Field("BroadcastChannel", const=True)})


BroadcastChannel.update_forward_refs()
