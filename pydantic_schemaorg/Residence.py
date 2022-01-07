from pydantic import Field
from pydantic_schemaorg.FloorPlan import FloorPlan
from typing import List, Optional, Union
from pydantic_schemaorg.Place import Place


class Residence(Place):
    """The place where a person lives.

    See https://schema.org/Residence.

    """
    type_: str = Field("Residence", const=True, alias='@type')
    accommodationFloorPlan: Optional[Union[List[Union[FloorPlan, str]], Union[FloorPlan, str]]] = Field(
        None,
        description="A floorplan of some [[Accommodation]].",
    )
    

Residence.update_forward_refs()
