from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom


class MedicalSign(MedicalSignOrSymptom):
    """Any physical manifestation of a person's medical condition discoverable by objective"
     "diagnostic tests or physical examination.

    See: https://schema.org/MedicalSign
    Model depth: 5
    """

    type_: str = Field("MedicalSign", const=True, alias="@type")
    identifyingExam: "Optional[Union[List[Union[PhysicalExam, str]], Union[PhysicalExam, str]]]" = Field(
        None,
        description="A physical examination that can identify this sign.",
    )
    identifyingTest: "Optional[Union[List[Union[MedicalTest, str]], Union[MedicalTest, str]]]" = Field(
        None,
        description="A diagnostic test that can identify this sign.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.PhysicalExam import PhysicalExam

    from pydantic_schemaorg.MedicalTest import MedicalTest

    MedicalSign.update_forward_refs()
