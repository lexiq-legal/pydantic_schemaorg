from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class BrainStructure(AnatomicalStructure):
    """Any anatomical structure which pertains to the soft nervous tissue functioning as the"
     "coordinating center of sensation and intellectual and nervous activity.

    See https://schema.org/BrainStructure.

    """

    locals().update({"@type": Field("BrainStructure", const=True)})


BrainStructure.update_forward_refs()
