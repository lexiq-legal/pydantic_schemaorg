from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class LegalValueLevel(Enumeration):
    """A list of possible levels for the legal validity of a legislation.

    See: https://schema.org/LegalValueLevel
    Model depth: 4
    """
    type_: str = Field("LegalValueLevel", alias='@type')
    

