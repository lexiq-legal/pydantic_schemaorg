from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Nerve(AnatomicalStructure):
    """A common pathway for the electrochemical nerve impulses that are transmitted along"
     "each of the axons.

    See: https://schema.org/Nerve
    Model depth: 4
    """

    type_: str = Field("Nerve", const=True, alias="@type")
    branch: "Optional[Union[List[Union[AnatomicalStructure, str]], Union[AnatomicalStructure, str]]]" = Field(
        None,
        description="The branches that delineate from the nerve bundle. Not to be confused with [[branchOf]].",
    )
    nerveMotor: "Optional[Union[List[Union[Muscle, str]], Union[Muscle, str]]]" = Field(
        None,
        description="The neurological pathway extension that involves muscle control.",
    )
    sensoryUnit: "Optional[Union[List[Union[SuperficialAnatomy, AnatomicalStructure, str]], Union[SuperficialAnatomy, AnatomicalStructure, str]]]" = Field(
        None,
        description="The neurological pathway extension that inputs and sends information to the brain or"
        "spinal cord.",
    )
    sourcedFrom: "Optional[Union[List[Union[BrainStructure, str]], Union[BrainStructure, str]]]" = Field(
        None,
        description="The neurological pathway that originates the neurons.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure

    from pydantic_schemaorg.Muscle import Muscle

    from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy

    from pydantic_schemaorg.BrainStructure import BrainStructure

    Nerve.update_forward_refs()
