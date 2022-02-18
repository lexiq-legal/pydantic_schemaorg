from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom


class MedicalSign(MedicalSignOrSymptom):
    """Any physical manifestation of a person's medical condition discoverable by objective"
     "diagnostic tests or physical examination.

    See: https://schema.org/MedicalSign
    Model depth: 5
    """
    type_: str = Field(default="MedicalSign", alias='@type', const=True)
    identifyingExam: Optional[Union[List[Union['PhysicalExam', str]], 'PhysicalExam', str]] = Field(
        default=None,
        description="A physical examination that can identify this sign.",
    )
    identifyingTest: Optional[Union[List[Union['MedicalTest', str]], 'MedicalTest', str]] = Field(
        default=None,
        description="A diagnostic test that can identify this sign.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.PhysicalExam import PhysicalExam
    from pydantic_schemaorg.MedicalTest import MedicalTest
