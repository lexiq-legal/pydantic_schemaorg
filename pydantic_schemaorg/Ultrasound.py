from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class Ultrasound(MedicalImagingTechnique):
    """Ultrasound imaging.

    See https://schema.org/Ultrasound.

    """
    type_: str = Field("Ultrasound", const=True, alias='@type')
    

Ultrasound.update_forward_refs()
