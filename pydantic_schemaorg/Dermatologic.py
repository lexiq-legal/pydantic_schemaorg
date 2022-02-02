from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dermatologic(MedicalSpecialty):
    """Something relating to or practicing dermatology.

    See: https://schema.org/Dermatologic
    Model depth: 6
    """
    type_: str = Field("Dermatologic", alias='@type')
    

