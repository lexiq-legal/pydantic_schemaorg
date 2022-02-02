from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class BrainStructure(AnatomicalStructure):
    """Any anatomical structure which pertains to the soft nervous tissue functioning as the"
     "coordinating center of sensation and intellectual and nervous activity.

    See: https://schema.org/BrainStructure
    Model depth: 4
    """
    type_: str = Field("BrainStructure", alias='@type')
    

