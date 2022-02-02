from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Genetic(MedicalSpecialty):
    """A specific branch of medical science that pertains to hereditary transmission and the"
     "variation of inherited characteristics and disorders.

    See: https://schema.org/Genetic
    Model depth: 6
    """
    type_: str = Field("Genetic", alias='@type')
    

