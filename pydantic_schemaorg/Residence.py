from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Place import Place


class Residence(Place):
    """The place where a person lives.

    See: https://schema.org/Residence
    Model depth: 3
    """
    type_: str = Field("Residence", alias='@type')
    accommodationFloorPlan: Optional[Union[List[Union['FloorPlan', str]], 'FloorPlan', str]] = Field(
        None,
        description="A floorplan of some [[Accommodation]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.FloorPlan import FloorPlan
