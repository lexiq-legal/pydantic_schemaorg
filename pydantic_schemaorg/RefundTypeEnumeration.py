from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class RefundTypeEnumeration(Enumeration):
    """Enumerates several kinds of product return refund types.

    See: https://schema.org/RefundTypeEnumeration
    Model depth: 4
    """
    type_: str = Field("RefundTypeEnumeration", alias='@type')
    

