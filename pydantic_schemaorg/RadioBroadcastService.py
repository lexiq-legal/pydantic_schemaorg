from pydantic import Field
from pydantic_schemaorg.BroadcastService import BroadcastService


class RadioBroadcastService(BroadcastService):
    """A delivery service through which radio content is provided via broadcast over the air"
     "or online.

    See https://schema.org/RadioBroadcastService.

    """
    type_: str = Field("RadioBroadcastService", const=True, alias='@type')
    

RadioBroadcastService.update_forward_refs()
