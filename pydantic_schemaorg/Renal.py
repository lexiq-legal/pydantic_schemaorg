from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Renal(MedicalSpecialty):
    """A specific branch of medical science that pertains to the study of the kidneys and its"
     "respective disease states.

    See: https://schema.org/Renal
    Model depth: 6
    """
    type_: str = Field("Renal", alias='@type')
    

