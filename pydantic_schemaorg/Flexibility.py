from pydantic import Field
from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory


class Flexibility(PhysicalActivityCategory):
    """Physical activity that is engaged in to improve joint and muscle flexibility.

    See https://schema.org/Flexibility.

    """
    type_: str = Field("Flexibility", const=True, alias='@type')
    

Flexibility.update_forward_refs()
