from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnlimitedWindow(MerchantReturnEnumeration):
    """Specifies that there is an unlimited window for product returns.

    See https://schema.org/MerchantReturnUnlimitedWindow.

    """
    type_: str = Field("MerchantReturnUnlimitedWindow", const=True, alias='@type')
    

MerchantReturnUnlimitedWindow.update_forward_refs()
