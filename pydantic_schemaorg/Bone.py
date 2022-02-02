from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Bone(AnatomicalStructure):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    See: https://schema.org/Bone
    Model depth: 4
    """
    type_: str = Field("Bone", alias='@type')
    

