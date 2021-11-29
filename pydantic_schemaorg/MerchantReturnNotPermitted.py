from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnNotPermitted(MerchantReturnEnumeration):
    """Specifies that product returns are not permitted.

    See https://schema.org/MerchantReturnNotPermitted.

    """

    locals().update({"@type": Field("MerchantReturnNotPermitted", const=True)})


MerchantReturnNotPermitted.update_forward_refs()
