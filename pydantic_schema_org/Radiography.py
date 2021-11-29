from pydantic import Field
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty
from pydantic_schema_org.MedicalImagingTechnique import MedicalImagingTechnique


class Radiography(MedicalSpecialty, MedicalImagingTechnique):
    """Radiography is an imaging technique that uses electromagnetic radiation other than"
     "visible light, especially X-rays, to view the internal structure of a non-uniformly"
     "composed and opaque object such as the human body.

    See https://schema.org/Radiography.

    """

    locals().update({"@type": Field("Radiography", const=True)})


Radiography.update_forward_refs()
