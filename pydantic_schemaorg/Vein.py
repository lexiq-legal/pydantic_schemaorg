from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from typing import List, Optional, Union
from pydantic_schemaorg.Vessel import Vessel
from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem


class Vein(Vessel):
    """A type of blood vessel that specifically carries blood to the heart.

    See https://schema.org/Vein.

    """
    type_: str = Field("Vein", const=True, alias='@type')
    tributary: Optional[Union[List[Union[AnatomicalStructure, str]], Union[AnatomicalStructure, str]]] = Field(
        None,
        description="The anatomical or organ system that the vein flows into; a larger structure that the vein"
     "connects to.",
    )
    drainsTo: Optional[Union[List[Union[Vessel, str]], Union[Vessel, str]]] = Field(
        None,
        description="The vasculature that the vein drains into.",
    )
    regionDrained: Optional[Union[List[Union[AnatomicalStructure, AnatomicalSystem, str]], Union[AnatomicalStructure, AnatomicalSystem, str]]] = Field(
        None,
        description="The anatomical or organ system drained by this vessel; generally refers to a specific"
     "part of an organ.",
    )
    

Vein.update_forward_refs()
