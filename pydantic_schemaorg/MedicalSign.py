from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam
from typing import Any, Optional, Union, List
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom


class MedicalSign(MedicalSignOrSymptom):
    """Any physical manifestation of a person's medical condition discoverable by objective"
     "diagnostic tests or physical examination.

    See https://schema.org/MedicalSign.

    """
    type_: str = Field("MedicalSign", const=True, alias='@type')
    identifyingExam: Optional[Union[List[PhysicalExam], PhysicalExam]] = Field(
        None,
        description="A physical examination that can identify this sign.",
    )
    identifyingTest: Optional[Union[List[MedicalTest], MedicalTest]] = Field(
        None,
        description="A diagnostic test that can identify this sign.",
    )
    

MedicalSign.update_forward_refs()
