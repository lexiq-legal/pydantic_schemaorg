from pydantic import Field
from pydantic_schema_org.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnUnlimitedWindow(MerchantReturnEnumeration):
    """Specifies that there is an unlimited window for product returns.

    See https://schema.org/MerchantReturnUnlimitedWindow.

    """

    locals().update({"@type": Field("MerchantReturnUnlimitedWindow", const=True)})


MerchantReturnUnlimitedWindow.update_forward_refs()
