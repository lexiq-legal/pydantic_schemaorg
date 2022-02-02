from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalIndication(MedicalEntity):
    """A condition or factor that indicates use of a medical therapy, including signs, symptoms,"
     "risk factors, anatomical states, etc.

    See: https://schema.org/MedicalIndication
    Model depth: 3
    """
    type_: str = Field("MedicalIndication", alias='@type')
    

