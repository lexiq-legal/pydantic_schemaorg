from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalImagingTechnique(MedicalEnumeration):
    """Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

    See: https://schema.org/MedicalImagingTechnique
    Model depth: 5
    """
    type_: str = Field("MedicalImagingTechnique", alias='@type')
    

