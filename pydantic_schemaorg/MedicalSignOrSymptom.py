from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalCondition import MedicalCondition


class MedicalSignOrSymptom(MedicalCondition):
    """Any feature associated or not with a medical condition. In medicine a symptom is generally"
     "subjective while a sign is objective.

    See: https://schema.org/MedicalSignOrSymptom
    Model depth: 4
    """
    type_: str = Field(default="MedicalSignOrSymptom", alias='@type', const=True)
    possibleTreatment: Optional[Union[List[Union['MedicalTherapy', str]], 'MedicalTherapy', str]] = Field(
        default=None,
        description="A possible treatment to address this condition, sign or symptom.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
