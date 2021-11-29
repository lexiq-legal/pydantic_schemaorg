from pydantic import Field
from pydantic_schemaorg.BroadcastService import BroadcastService


class RadioBroadcastService(BroadcastService):
    """A delivery service through which radio content is provided via broadcast over the air"
     "or online.

    See https://schema.org/RadioBroadcastService.

    """

    locals().update({"@type": Field("RadioBroadcastService", const=True)})


RadioBroadcastService.update_forward_refs()
