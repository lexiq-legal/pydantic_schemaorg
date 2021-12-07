from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class StatusEnumeration(Enumeration):
    """Lists or enumerations dealing with status types.

    See https://schema.org/StatusEnumeration.

    """
    type_: str = Field("StatusEnumeration", const=True, alias='@type')
    

StatusEnumeration.update_forward_refs()
