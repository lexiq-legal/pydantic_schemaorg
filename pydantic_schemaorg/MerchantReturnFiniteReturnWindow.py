from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnFiniteReturnWindow(MerchantReturnEnumeration):
    """Specifies that there is a finite window for product returns.

    See https://schema.org/MerchantReturnFiniteReturnWindow.

    """
    type_: str = Field("MerchantReturnFiniteReturnWindow", const=True, alias='@type')
    

MerchantReturnFiniteReturnWindow.update_forward_refs()
