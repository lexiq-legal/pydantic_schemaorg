from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """Car repair business.

    See: https://schema.org/AutoRepair
    Model depth: 5
    """
    type_: str = Field("AutoRepair", alias='@type')
    

