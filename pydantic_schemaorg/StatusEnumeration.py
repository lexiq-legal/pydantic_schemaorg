from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class StatusEnumeration(Enumeration):
    """Lists or enumerations dealing with status types.

    See: https://schema.org/StatusEnumeration
    Model depth: 4
    """
    type_: str = Field("StatusEnumeration", alias='@type')
    

