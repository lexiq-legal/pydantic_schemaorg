from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ReturnLabelSourceEnumeration(Enumeration):
    """Enumerates several types of return labels for product returns.

    See https://schema.org/ReturnLabelSourceEnumeration.

    """
    type_: str = Field("ReturnLabelSourceEnumeration", const=True, alias='@type')
    

ReturnLabelSourceEnumeration.update_forward_refs()
