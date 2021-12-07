from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnNotPermitted(MerchantReturnEnumeration):
    """Specifies that product returns are not permitted.

    See https://schema.org/MerchantReturnNotPermitted.

    """
    type_: str = Field("MerchantReturnNotPermitted", const=True, alias='@type')
    

MerchantReturnNotPermitted.update_forward_refs()
