from pydantic import Field
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class LeisureTimeActivity(PhysicalActivityCategory):
    """Any physical activity engaged in for recreational purposes. Examples may include ballroom"
     "dancing, roller skating, canoeing, fishing, etc.

    See https://schema.org/LeisureTimeActivity.

    """
    type_: str = Field("LeisureTimeActivity", const=True, alias='@type')
    

LeisureTimeActivity.update_forward_refs()
