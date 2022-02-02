from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoBodyShop(AutomotiveBusiness):
    """Auto body shop.

    See: https://schema.org/AutoBodyShop
    Model depth: 5
    """
    type_: str = Field("AutoBodyShop", alias='@type')
    

