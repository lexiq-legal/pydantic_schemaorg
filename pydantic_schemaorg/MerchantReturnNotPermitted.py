from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnNotPermitted(MerchantReturnEnumeration):
    """Specifies that product returns are not permitted.

    See: https://schema.org/MerchantReturnNotPermitted
    Model depth: 5
    """
    type_: str = Field("MerchantReturnNotPermitted", alias='@type')
    

