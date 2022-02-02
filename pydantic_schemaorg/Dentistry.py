from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dentistry(MedicalSpecialty):
    """A branch of medicine that is involved in the dental care.

    See: https://schema.org/Dentistry
    Model depth: 6
    """
    type_: str = Field("Dentistry", alias='@type')
    

