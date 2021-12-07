from pydantic import Field
from pydantic_schemaorg.GenderType import GenderType


class Male(GenderType):
    """The male gender.

    See https://schema.org/Male.

    """
    type_: str = Field("Male", const=True, alias='@type')
    

Male.update_forward_refs()
