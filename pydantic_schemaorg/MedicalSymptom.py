from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom


class MedicalSymptom(MedicalSignOrSymptom):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)"
     "like stomachache, lower-back pain, or fatigue.

    See: https://schema.org/MedicalSymptom
    Model depth: 5
    """
    type_: str = Field("MedicalSymptom", alias='@type')
    

