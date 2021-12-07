from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class RefundTypeEnumeration(Enumeration):
    """Enumerates several kinds of product return refund types.

    See https://schema.org/RefundTypeEnumeration.

    """
    type_: str = Field("RefundTypeEnumeration", const=True, alias='@type')
    

RefundTypeEnumeration.update_forward_refs()
