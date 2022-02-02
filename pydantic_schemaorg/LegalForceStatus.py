from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class LegalForceStatus(StatusEnumeration):
    """A list of possible statuses for the legal force of a legislation.

    See: https://schema.org/LegalForceStatus
    Model depth: 5
    """
    type_: str = Field("LegalForceStatus", alias='@type')
    

