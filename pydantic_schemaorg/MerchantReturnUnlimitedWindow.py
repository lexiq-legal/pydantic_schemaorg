from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnlimitedWindow(MerchantReturnEnumeration):
    """Specifies that there is an unlimited window for product returns.

    See: https://schema.org/MerchantReturnUnlimitedWindow
    Model depth: 5
    """
    type_: str = Field("MerchantReturnUnlimitedWindow", alias='@type')
    

