from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Museum(CivicStructure):
    """A museum.

    See https://schema.org/Museum.

    """
    type_: str = Field("Museum", const=True, alias='@type')
    

Museum.update_forward_refs()
