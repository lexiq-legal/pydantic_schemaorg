from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MerchantReturnEnumeration(Enumeration):
    """Enumerates several kinds of product return policies.

    See https://schema.org/MerchantReturnEnumeration.

    """
    type_: str = Field("MerchantReturnEnumeration", const=True, alias='@type')
    

MerchantReturnEnumeration.update_forward_refs()
