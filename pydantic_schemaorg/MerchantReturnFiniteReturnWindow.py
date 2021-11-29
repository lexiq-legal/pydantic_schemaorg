from pydantic import Field
from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration


class MerchantReturnFiniteReturnWindow(MerchantReturnEnumeration):
    """Specifies that there is a finite window for product returns.

    See https://schema.org/MerchantReturnFiniteReturnWindow.

    """

    locals().update({"@type": Field("MerchantReturnFiniteReturnWindow", const=True)})


MerchantReturnFiniteReturnWindow.update_forward_refs()
