from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Bone(AnatomicalStructure):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    See: https://schema.org/Bone
    Model depth: 4
    """

    type_: str = Field("Bone", const=True, alias="@type")


if TYPE_CHECKING:

    Bone.update_forward_refs()
