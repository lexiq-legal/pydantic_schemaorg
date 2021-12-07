from pydantic import Field
from pydantic_schemaorg.LegalForceStatus import LegalForceStatus


class InForce(LegalForceStatus):
    """Indicates that a legislation is in force.

    See https://schema.org/InForce.

    """
    type_: str = Field("InForce", const=True, alias='@type')
    

InForce.update_forward_refs()
