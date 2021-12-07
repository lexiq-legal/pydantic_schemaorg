from pydantic import Field
from pydantic_schemaorg.Event import Event


class SaleEvent(Event):
    """Event type: Sales event.

    See https://schema.org/SaleEvent.

    """
    type_: str = Field("SaleEvent", const=True, alias='@type')
    

SaleEvent.update_forward_refs()
