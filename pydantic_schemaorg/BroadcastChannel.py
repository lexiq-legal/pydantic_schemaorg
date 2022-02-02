from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class BroadcastChannel(Intangible):
    """A unique instance of a BroadcastService on a CableOrSatelliteService lineup.

    See: https://schema.org/BroadcastChannel
    Model depth: 3
    """
    type_: str = Field("BroadcastChannel", alias='@type')
    broadcastChannelId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The unique address by which the BroadcastService can be identified in a provider lineup."
     "In US, this is typically a number.",
    )
    broadcastFrequency: Optional[Union[List[Union[str, 'Text', 'BroadcastFrequencySpecification']], str, 'Text', 'BroadcastFrequencySpecification']] = Field(
        None,
        description="The frequency used for over-the-air broadcasts. Numeric values or simple ranges e.g."
     "87-99. In addition a shortcut idiom is supported for frequences of AM and FM radio channels,"
     "e.g. \"87 FM\".",
    )
    genre: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    providesBroadcastService: Optional[Union[List[Union['BroadcastService', str]], 'BroadcastService', str]] = Field(
        None,
        description="The BroadcastService offered on this channel.",
    )
    broadcastServiceTier: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The type of service required to have access to the channel (e.g. Standard or Premium).",
    )
    inBroadcastLineup: Optional[Union[List[Union['CableOrSatelliteService', str]], 'CableOrSatelliteService', str]] = Field(
        None,
        description="The CableOrSatelliteService offering the channel.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BroadcastFrequencySpecification import BroadcastFrequencySpecification
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.BroadcastService import BroadcastService
    from pydantic_schemaorg.CableOrSatelliteService import CableOrSatelliteService
