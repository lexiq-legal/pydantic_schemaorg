from pydantic import Field
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class AnaerobicActivity(PhysicalActivityCategory):
    """Physical activity that is of high-intensity which utilizes the anaerobic metabolism"
     "of the body.

    See https://schema.org/AnaerobicActivity.

    """
    type_: str = Field("AnaerobicActivity", const=True, alias='@type')
    

AnaerobicActivity.update_forward_refs()
