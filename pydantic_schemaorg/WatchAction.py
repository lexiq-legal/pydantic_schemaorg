from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class WatchAction(ConsumeAction):
    """The act of consuming dynamic/moving visual content.

    See https://schema.org/WatchAction.

    """
    type_: str = Field("WatchAction", const=True, alias='@type')
    

WatchAction.update_forward_refs()
