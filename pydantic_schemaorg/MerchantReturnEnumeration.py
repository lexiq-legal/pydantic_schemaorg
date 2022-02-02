from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MerchantReturnEnumeration(Enumeration):
    """Enumerates several kinds of product return policies.

    See: https://schema.org/MerchantReturnEnumeration
    Model depth: 4
    """
    type_: str = Field("MerchantReturnEnumeration", alias='@type')
    

