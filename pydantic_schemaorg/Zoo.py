from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Zoo(CivicStructure):
    """A zoo.

    See https://schema.org/Zoo.

    """
    type_: str = Field("Zoo", const=True, alias='@type')
    

Zoo.update_forward_refs()
