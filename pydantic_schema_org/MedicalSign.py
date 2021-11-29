from pydantic import Field
from pydantic_schema_org.PhysicalExam import PhysicalExam
from typing import Any, Optional, Union, List
from pydantic_schema_org.MedicalTest import MedicalTest
from pydantic_schema_org.MedicalSignOrSymptom import MedicalSignOrSymptom


class MedicalSign(MedicalSignOrSymptom):
    """Any physical manifestation of a person's medical condition discoverable by objective"
     "diagnostic tests or physical examination.

    See https://schema.org/MedicalSign.

    """

    identifyingExam: Optional[Union[List[PhysicalExam], PhysicalExam]] = Field(
        None,
        description="A physical examination that can identify this sign.",
    )
    identifyingTest: Optional[Union[List[MedicalTest], MedicalTest]] = Field(
        None,
        description="A diagnostic test that can identify this sign.",
    )
    locals().update({"@type": Field("MedicalSign", const=True)})


MedicalSign.update_forward_refs()
