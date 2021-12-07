from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnspecified(MerchantReturnEnumeration):
    """Specifies that a product return policy is not provided.

    See https://schema.org/MerchantReturnUnspecified.

    """
    type_: str = Field("MerchantReturnUnspecified", const=True, alias='@type')
    

MerchantReturnUnspecified.update_forward_refs()
