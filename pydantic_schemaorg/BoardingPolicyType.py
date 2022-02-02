from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class BoardingPolicyType(Enumeration):
    """A type of boarding policy used by an airline.

    See: https://schema.org/BoardingPolicyType
    Model depth: 4
    """
    type_: str = Field("BoardingPolicyType", alias='@type')
    

