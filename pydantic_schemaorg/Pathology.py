from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Pathology(MedicalSpecialty):
    """A specific branch of medical science that is concerned with the study of the cause, origin"
     "and nature of a disease state, including its consequences as a result of manifestation"
     "of the disease. In clinical care, the term is used to designate a branch of medicine using"
     "laboratory tests to diagnose and determine the prognostic significance of illness.

    See: https://schema.org/Pathology
    Model depth: 6
    """
    type_: str = Field("Pathology", alias='@type')
    

