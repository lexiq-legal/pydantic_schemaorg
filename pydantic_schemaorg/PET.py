from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class PET(MedicalImagingTechnique):
    """Positron emission tomography imaging.

    See: https://schema.org/PET
    Model depth: 6
    """
    type_: str = Field("PET", alias='@type')
    

