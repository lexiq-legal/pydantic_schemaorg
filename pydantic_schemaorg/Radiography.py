from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class Radiography(MedicalSpecialty, MedicalImagingTechnique):
    """Radiography is an imaging technique that uses electromagnetic radiation other than"
     "visible light, especially X-rays, to view the internal structure of a non-uniformly"
     "composed and opaque object such as the human body.

    See: https://schema.org/Radiography
    Model depth: 6
    """
    type_: str = Field("Radiography", alias='@type')
    

