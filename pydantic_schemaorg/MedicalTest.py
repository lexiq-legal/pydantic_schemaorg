from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalTest(MedicalEntity):
    """Any medical test, typically performed for diagnostic purposes.

    See: https://schema.org/MedicalTest
    Model depth: 3
    """

    type_: str = Field("MedicalTest", const=True, alias="@type")
    usesDevice: "Optional[Union[List[Union[MedicalDevice, str]], Union[MedicalDevice, str]]]" = Field(
        None,
        description="Device used to perform the test.",
    )
    normalRange: "Optional[Union[List[Union[str, MedicalEnumeration]], Union[str, MedicalEnumeration]]]" = Field(
        None,
        description="Range of acceptable values for a typical patient, when applicable.",
    )
    affectedBy: "Optional[Union[List[Union[Drug, str]], Union[Drug, str]]]" = Field(
        None,
        description="Drugs that affect the test's results.",
    )
    signDetected: "Optional[Union[List[Union[MedicalSign, str]], Union[MedicalSign, str]]]" = Field(
        None,
        description="A sign detected by the test.",
    )
    usedToDiagnose: "Optional[Union[List[Union[MedicalCondition, str]], Union[MedicalCondition, str]]]" = Field(
        None,
        description="A condition the test is used to diagnose.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalDevice import MedicalDevice

    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration

    from pydantic_schemaorg.Drug import Drug

    from pydantic_schemaorg.MedicalSign import MedicalSign

    from pydantic_schemaorg.MedicalCondition import MedicalCondition

    MedicalTest.update_forward_refs()
