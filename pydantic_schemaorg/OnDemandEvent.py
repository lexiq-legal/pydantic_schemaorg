from pydantic import Field
from pydantic_schemaorg.PublicationEvent import PublicationEvent


class OnDemandEvent(PublicationEvent):
    """A publication event e.g. catch-up TV or radio podcast, during which a program is available"
     "on-demand.

    See https://schema.org/OnDemandEvent.

    """
    type_: str = Field("OnDemandEvent", const=True, alias='@type')
    

OnDemandEvent.update_forward_refs()
