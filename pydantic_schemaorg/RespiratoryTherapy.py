from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class RespiratoryTherapy(MedicalSpecialty, MedicalTherapy):
    """The therapy that is concerned with the maintenance or improvement of respiratory function"
     "(as in patients with pulmonary disease).

    See: https://schema.org/RespiratoryTherapy
    Model depth: 6
    """
    type_: str = Field(default="RespiratoryTherapy", alias='@type')
    
