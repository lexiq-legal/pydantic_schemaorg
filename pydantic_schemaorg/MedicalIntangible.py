from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalIntangible(MedicalEntity):
    """A utility class that serves as the umbrella for a number of 'intangible' things in the"
     "medical space.

    See https://schema.org/MedicalIntangible.

    """
    type_: str = Field("MedicalIntangible", const=True, alias='@type')
    

MedicalIntangible.update_forward_refs()
