from pydantic import Field
from pydantic_schemaorg.Vessel import Vessel
from typing import List, Optional, Union
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem


class LymphaticVessel(Vessel):
    """A type of blood vessel that specifically carries lymph fluid unidirectionally toward"
     "the heart.

    See https://schema.org/LymphaticVessel.

    """
    type_: str = Field("LymphaticVessel", const=True, alias='@type')
    originatesFrom: Optional[Union[List[Union[Vessel, str]], Union[Vessel, str]]] = Field(
        None,
        description="The vasculature the lymphatic structure originates, or afferents, from.",
    )
    runsTo: Optional[Union[List[Union[Vessel, str]], Union[Vessel, str]]] = Field(
        None,
        description="The vasculature the lymphatic structure runs, or efferents, to.",
    )
    regionDrained: Optional[Union[List[Union[AnatomicalStructure, AnatomicalSystem, str]], Union[AnatomicalStructure, AnatomicalSystem, str]]] = Field(
        None,
        description="The anatomical or organ system drained by this vessel; generally refers to a specific"
     "part of an organ.",
    )
    

LymphaticVessel.update_forward_refs()
