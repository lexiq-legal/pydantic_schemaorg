from pydantic import Field
from pydantic_schemaorg.LegalForceStatus import LegalForceStatus


class NotInForce(LegalForceStatus):
    """Indicates that a legislation is currently not in force.

    See https://schema.org/NotInForce.

    """
    type_: str = Field("NotInForce", const=True, alias='@type')
    

NotInForce.update_forward_refs()
