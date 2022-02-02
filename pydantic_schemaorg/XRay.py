from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class XRay(MedicalImagingTechnique):
    """X-ray imaging.

    See: https://schema.org/XRay
    Model depth: 6
    """
    type_: str = Field("XRay", alias='@type')
    

