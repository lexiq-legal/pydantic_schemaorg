from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Playground(CivicStructure):
    """A playground.

    See https://schema.org/Playground.

    """
    type_: str = Field("Playground", const=True, alias='@type')
    

Playground.update_forward_refs()
