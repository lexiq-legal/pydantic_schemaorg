from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Park(CivicStructure):
    """A park.

    See https://schema.org/Park.

    """
    type_: str = Field("Park", const=True, alias='@type')
    

Park.update_forward_refs()
