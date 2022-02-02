from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class RVPark(CivicStructure):
    """A place offering space for \"Recreational Vehicles\", Caravans, mobile homes and the"
     "like.

    See: https://schema.org/RVPark
    Model depth: 4
    """
    type_: str = Field("RVPark", alias='@type')
    

