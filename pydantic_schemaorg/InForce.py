from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LegalForceStatus import LegalForceStatus


class InForce(LegalForceStatus):
    """Indicates that a legislation is in force.

    See: https://schema.org/InForce
    Model depth: 6
    """
    type_: str = Field("InForce", alias='@type')
    

