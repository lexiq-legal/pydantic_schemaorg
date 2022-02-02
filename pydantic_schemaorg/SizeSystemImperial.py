from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemImperial(SizeSystemEnumeration):
    """Imperial size system.

    See: https://schema.org/SizeSystemImperial
    Model depth: 5
    """
    type_: str = Field("SizeSystemImperial", alias='@type')
    

