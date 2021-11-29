from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ReturnLabelSourceEnumeration(Enumeration):
    """Enumerates several types of return labels for product returns.

    See https://schema.org/ReturnLabelSourceEnumeration.

    """

    locals().update({"@type": Field("ReturnLabelSourceEnumeration", const=True)})


ReturnLabelSourceEnumeration.update_forward_refs()
