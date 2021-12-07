from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Bone(AnatomicalStructure):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    See https://schema.org/Bone.

    """
    type_: str = Field("Bone", const=True, alias='@type')
    

Bone.update_forward_refs()
