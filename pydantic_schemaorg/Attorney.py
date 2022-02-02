from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LegalService import LegalService


class Attorney(LegalService):
    """Professional service: Attorney. This type is deprecated - [[LegalService]] is more"
     "inclusive and less ambiguous.

    See: https://schema.org/Attorney
    Model depth: 5
    """
    type_: str = Field("Attorney", alias='@type')
    

