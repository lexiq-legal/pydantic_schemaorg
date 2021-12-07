from pydantic import Field
from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom


class MedicalSymptom(MedicalSignOrSymptom):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)"
     "like stomachache, lower-back pain, or fatigue.

    See https://schema.org/MedicalSymptom.

    """
    type_: str = Field("MedicalSymptom", const=True, alias='@type')
    

MedicalSymptom.update_forward_refs()
