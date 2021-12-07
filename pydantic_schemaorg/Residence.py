from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Place import Place


class Residence(Place):
    """The place where a person lives.

    See https://schema.org/Residence.

    """
    type_: str = Field("Residence", const=True, alias='@type')
    accommodationFloorPlan: Any = Field(
        None,
        description="A floorplan of some [[Accommodation]].",
    )
    

Residence.update_forward_refs()
