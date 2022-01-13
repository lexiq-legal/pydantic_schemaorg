from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Vessel import Vessel


class Vein(Vessel):
    """A type of blood vessel that specifically carries blood to the heart.

    See: https://schema.org/Vein
    Model depth: 5
    """

    type_: str = Field("Vein", const=True, alias="@type")
    tributary: "Optional[Union[List[Union[AnatomicalStructure, str]], Union[AnatomicalStructure, str]]]" = Field(
        None,
        description="The anatomical or organ system that the vein flows into; a larger structure that the vein"
        "connects to.",
    )
    drainsTo: "Optional[Union[List[Union[Vessel, str]], Union[Vessel, str]]]" = Field(
        None,
        description="The vasculature that the vein drains into.",
    )
    regionDrained: "Optional[Union[List[Union[AnatomicalSystem, AnatomicalStructure, str]], Union[AnatomicalSystem, AnatomicalStructure, str]]]" = Field(
        None,
        description="The anatomical or organ system drained by this vessel; generally refers to a specific"
        "part of an organ.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure

    from pydantic_schemaorg.Vessel import Vessel

    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem

    Vein.update_forward_refs()
