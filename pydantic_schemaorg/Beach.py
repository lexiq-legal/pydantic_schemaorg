from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Beach(CivicStructure):
    """Beach.

    See https://schema.org/Beach.

    """
    type_: str = Field("Beach", const=True, alias='@type')
    

Beach.update_forward_refs()
