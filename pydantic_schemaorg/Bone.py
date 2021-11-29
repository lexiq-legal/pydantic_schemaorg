from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Bone(AnatomicalStructure):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    See https://schema.org/Bone.

    """

    locals().update({"@type": Field("Bone", const=True)})


Bone.update_forward_refs()
