from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class RefundTypeEnumeration(Enumeration):
    """Enumerates several kinds of product return refund types.

    See https://schema.org/RefundTypeEnumeration.

    """

    locals().update({"@type": Field("RefundTypeEnumeration", const=True)})


RefundTypeEnumeration.update_forward_refs()
