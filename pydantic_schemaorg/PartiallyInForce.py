from pydantic import Field
from pydantic_schemaorg.LegalForceStatus import LegalForceStatus


class PartiallyInForce(LegalForceStatus):
    """Indicates that parts of the legislation are in force, and parts are not.

    See https://schema.org/PartiallyInForce.

    """
    type_: str = Field("PartiallyInForce", const=True, alias='@type')
    

PartiallyInForce.update_forward_refs()
