from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """A car wash business.

    See: https://schema.org/AutoWash
    Model depth: 5
    """
    type_: str = Field("AutoWash", alias='@type')
    

