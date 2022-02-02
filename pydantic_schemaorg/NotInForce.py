from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LegalForceStatus import LegalForceStatus


class NotInForce(LegalForceStatus):
    """Indicates that a legislation is currently not in force.

    See: https://schema.org/NotInForce
    Model depth: 6
    """
    type_: str = Field("NotInForce", alias='@type')
    

