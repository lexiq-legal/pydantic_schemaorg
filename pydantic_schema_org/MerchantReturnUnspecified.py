from pydantic import Field
from pydantic_schema_org.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnspecified(MerchantReturnEnumeration):
    """Specifies that a product return policy is not provided.

    See https://schema.org/MerchantReturnUnspecified.

    """

    locals().update({"@type": Field("MerchantReturnUnspecified", const=True)})


MerchantReturnUnspecified.update_forward_refs()
