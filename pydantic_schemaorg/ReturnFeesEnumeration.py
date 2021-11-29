from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ReturnFeesEnumeration(Enumeration):
    """Enumerates several kinds of policies for product return fees.

    See https://schema.org/ReturnFeesEnumeration.

    """

    locals().update({"@type": Field("ReturnFeesEnumeration", const=True)})


ReturnFeesEnumeration.update_forward_refs()
