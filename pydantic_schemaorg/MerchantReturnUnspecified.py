from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnspecified(MerchantReturnEnumeration):
    """Specifies that a product return policy is not provided.

    See https://schema.org/MerchantReturnUnspecified.

    """

    locals().update({"@type": Field("MerchantReturnUnspecified", const=True)})


MerchantReturnUnspecified.update_forward_refs()
