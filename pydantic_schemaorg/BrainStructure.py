from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class BrainStructure(AnatomicalStructure):
    """Any anatomical structure which pertains to the soft nervous tissue functioning as the"
     "coordinating center of sensation and intellectual and nervous activity.

    See https://schema.org/BrainStructure.

    """
    type_: str = Field("BrainStructure", const=True, alias='@type')
    

BrainStructure.update_forward_refs()
