from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class GenderType(Enumeration):
    """An enumeration of genders.

    See https://schema.org/GenderType.

    """
    type_: str = Field("GenderType", const=True, alias='@type')
    

GenderType.update_forward_refs()
