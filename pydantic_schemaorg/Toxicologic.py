from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Toxicologic(MedicalSpecialty):
    """A specific branch of medical science that is concerned with poisons, their nature, effects"
     "and detection and involved in the treatment of poisoning.

    See: https://schema.org/Toxicologic
    Model depth: 6
    """
    type_: str = Field("Toxicologic", alias='@type')
    

