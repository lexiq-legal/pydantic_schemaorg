from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class Ultrasound(MedicalImagingTechnique):
    """Ultrasound imaging.

    See: https://schema.org/Ultrasound
    Model depth: 6
    """
    type_: str = Field("Ultrasound", alias='@type')
    

