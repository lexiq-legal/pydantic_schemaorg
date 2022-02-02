from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class OccupationalTherapy(MedicalTherapy):
    """A treatment of people with physical, emotional, or social problems, using purposeful"
     "activity to help them overcome or learn to deal with their problems.

    See: https://schema.org/OccupationalTherapy
    Model depth: 6
    """
    type_: str = Field("OccupationalTherapy", alias='@type')
    

