from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class LegalForceStatus(StatusEnumeration):
    """A list of possible statuses for the legal force of a legislation.

    See https://schema.org/LegalForceStatus.

    """
    type_: str = Field("LegalForceStatus", const=True, alias='@type')
    

LegalForceStatus.update_forward_refs()
