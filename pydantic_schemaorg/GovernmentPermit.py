from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Permit import Permit


class GovernmentPermit(Permit):
    """A permit issued by a government agency.

    See: https://schema.org/GovernmentPermit
    Model depth: 4
    """
    type_: str = Field("GovernmentPermit", alias='@type')
    

