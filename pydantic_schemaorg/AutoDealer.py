from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoDealer(AutomotiveBusiness):
    """An car dealership.

    See: https://schema.org/AutoDealer
    Model depth: 5
    """
    type_: str = Field("AutoDealer", alias='@type')
    

