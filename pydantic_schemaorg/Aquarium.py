from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Aquarium(CivicStructure):
    """Aquarium.

    See https://schema.org/Aquarium.

    """
    type_: str = Field("Aquarium", const=True, alias='@type')
    

Aquarium.update_forward_refs()
