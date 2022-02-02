from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class MRI(MedicalImagingTechnique):
    """Magnetic resonance imaging.

    See: https://schema.org/MRI
    Model depth: 6
    """
    type_: str = Field("MRI", alias='@type')
    

