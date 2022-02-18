from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class CT(MedicalImagingTechnique):
    """X-ray computed tomography imaging.

    See: https://schema.org/CT
    Model depth: 6
    """
    type_: str = Field(default="CT", alias='@type', const=True)
    
