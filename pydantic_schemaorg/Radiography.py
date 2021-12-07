from pydantic import Field
from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Radiography(MedicalImagingTechnique, MedicalSpecialty):
    """Radiography is an imaging technique that uses electromagnetic radiation other than"
     "visible light, especially X-rays, to view the internal structure of a non-uniformly"
     "composed and opaque object such as the human body.

    See https://schema.org/Radiography.

    """
    type_: str = Field("Radiography", const=True, alias='@type')
    

Radiography.update_forward_refs()
