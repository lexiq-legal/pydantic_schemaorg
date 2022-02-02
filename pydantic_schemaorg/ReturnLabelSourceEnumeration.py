from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ReturnLabelSourceEnumeration(Enumeration):
    """Enumerates several types of return labels for product returns.

    See: https://schema.org/ReturnLabelSourceEnumeration
    Model depth: 4
    """
    type_: str = Field("ReturnLabelSourceEnumeration", alias='@type')
    

