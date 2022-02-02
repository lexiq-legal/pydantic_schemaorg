from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LegalForceStatus import LegalForceStatus


class PartiallyInForce(LegalForceStatus):
    """Indicates that parts of the legislation are in force, and parts are not.

    See: https://schema.org/PartiallyInForce
    Model depth: 6
    """
    type_: str = Field("PartiallyInForce", alias='@type')
    

