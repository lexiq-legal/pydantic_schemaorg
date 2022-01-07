from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from typing import List, Optional, Union
from pydantic_schemaorg.MedicalCondition import MedicalCondition


class MedicalSignOrSymptom(MedicalCondition):
    """Any feature associated or not with a medical condition. In medicine a symptom is generally"
     "subjective while a sign is objective.

    See https://schema.org/MedicalSignOrSymptom.

    """
    type_: str = Field("MedicalSignOrSymptom", const=True, alias='@type')
    possibleTreatment: Optional[Union[List[Union[MedicalTherapy, str]], Union[MedicalTherapy, str]]] = Field(
        None,
        description="A possible treatment to address this condition, sign or symptom.",
    )
    

MedicalSignOrSymptom.update_forward_refs()
