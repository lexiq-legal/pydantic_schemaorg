from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MerchantReturnEnumeration(Enumeration):
    """Enumerates several kinds of product return policies.

    See https://schema.org/MerchantReturnEnumeration.

    """

    locals().update({"@type": Field("MerchantReturnEnumeration", const=True)})


MerchantReturnEnumeration.update_forward_refs()
