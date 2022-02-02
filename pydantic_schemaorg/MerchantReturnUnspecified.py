from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnspecified(MerchantReturnEnumeration):
    """Specifies that a product return policy is not provided.

    See: https://schema.org/MerchantReturnUnspecified
    Model depth: 5
    """
    type_: str = Field("MerchantReturnUnspecified", alias='@type')
    

