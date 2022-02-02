from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Nerve(AnatomicalStructure):
    """A common pathway for the electrochemical nerve impulses that are transmitted along"
     "each of the axons.

    See: https://schema.org/Nerve
    Model depth: 4
    """
    type_: str = Field("Nerve", alias='@type')
    branch: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        None,
        description="The branches that delineate from the nerve bundle. Not to be confused with [[branchOf]].",
    )
    nerveMotor: Optional[Union[List[Union['Muscle', str]], 'Muscle', str]] = Field(
        None,
        description="The neurological pathway extension that involves muscle control.",
    )
    sensoryUnit: Optional[Union[List[Union['SuperficialAnatomy', 'AnatomicalStructure', str]], 'SuperficialAnatomy', 'AnatomicalStructure', str]] = Field(
        None,
        description="The neurological pathway extension that inputs and sends information to the brain or"
     "spinal cord.",
    )
    sourcedFrom: Optional[Union[List[Union['BrainStructure', str]], 'BrainStructure', str]] = Field(
        None,
        description="The neurological pathway that originates the neurons.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.Muscle import Muscle
    from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy
    from pydantic_schemaorg.BrainStructure import BrainStructure
