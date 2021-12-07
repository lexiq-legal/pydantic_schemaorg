from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Cemetery(CivicStructure):
    """A graveyard.

    See https://schema.org/Cemetery.

    """
    type_: str = Field("Cemetery", const=True, alias='@type')
    

Cemetery.update_forward_refs()
