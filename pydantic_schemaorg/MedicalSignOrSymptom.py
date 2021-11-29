from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalCondition import MedicalCondition


class MedicalSignOrSymptom(MedicalCondition):
    """Any feature associated or not with a medical condition. In medicine a symptom is generally"
     "subjective while a sign is objective.

    See https://schema.org/MedicalSignOrSymptom.

    """

    possibleTreatment: Optional[Union[List[MedicalTherapy], MedicalTherapy]] = Field(
        None,
        description="A possible treatment to address this condition, sign or symptom.",
    )
    locals().update({"@type": Field("MedicalSignOrSymptom", const=True)})


MedicalSignOrSymptom.update_forward_refs()
