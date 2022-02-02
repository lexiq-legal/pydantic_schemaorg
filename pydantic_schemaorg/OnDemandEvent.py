from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PublicationEvent import PublicationEvent


class OnDemandEvent(PublicationEvent):
    """A publication event e.g. catch-up TV or radio podcast, during which a program is available"
     "on-demand.

    See: https://schema.org/OnDemandEvent
    Model depth: 4
    """
    type_: str = Field("OnDemandEvent", alias='@type')
    

