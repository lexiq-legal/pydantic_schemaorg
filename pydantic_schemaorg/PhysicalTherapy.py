from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class PhysicalTherapy(MedicalTherapy):
    """A process of progressive physical care and rehabilitation aimed at improving a health"
     "condition.

    See: https://schema.org/PhysicalTherapy
    Model depth: 6
    """
    type_: str = Field("PhysicalTherapy", alias='@type')
    

