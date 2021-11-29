from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ReturnMethodEnumeration(Enumeration):
    """Enumerates several types of product return methods.

    See https://schema.org/ReturnMethodEnumeration.

    """

    locals().update({"@type": Field("ReturnMethodEnumeration", const=True)})


ReturnMethodEnumeration.update_forward_refs()
