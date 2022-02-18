from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Vessel import Vessel


class LymphaticVessel(Vessel):
    """A type of blood vessel that specifically carries lymph fluid unidirectionally toward"
     "the heart.

    See: https://schema.org/LymphaticVessel
    Model depth: 5
    """
    type_: str = Field(default="LymphaticVessel", alias='@type', constant=True)
    originatesFrom: Optional[Union[List[Union['Vessel', str]], 'Vessel', str]] = Field(
        default=None,
        description="The vasculature the lymphatic structure originates, or afferents, from.",
    )
    runsTo: Optional[Union[List[Union['Vessel', str]], 'Vessel', str]] = Field(
        default=None,
        description="The vasculature the lymphatic structure runs, or efferents, to.",
    )
    regionDrained: Optional[Union[List[Union['AnatomicalStructure', 'AnatomicalSystem', str]], 'AnatomicalStructure', 'AnatomicalSystem', str]] = Field(
        default=None,
        description="The anatomical or organ system drained by this vessel; generally refers to a specific"
     "part of an organ.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Vessel import Vessel
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
