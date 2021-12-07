from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class RVPark(CivicStructure):
    """A place offering space for \"Recreational Vehicles\", Caravans, mobile homes and the"
     "like.

    See https://schema.org/RVPark.

    """
    type_: str = Field("RVPark", const=True, alias='@type')
    

RVPark.update_forward_refs()
