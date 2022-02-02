from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class AutomotiveBusiness(LocalBusiness):
    """Car repair, sales, or parts.

    See: https://schema.org/AutomotiveBusiness
    Model depth: 4
    """
    type_: str = Field("AutomotiveBusiness", alias='@type')
    

