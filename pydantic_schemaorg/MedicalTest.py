from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalTest(MedicalEntity):
    """Any medical test, typically performed for diagnostic purposes.

    See https://schema.org/MedicalTest.

    """

    usesDevice: Any = Field(
        None,
        description="Device used to perform the test.",
    )
    normalRange: Optional[Union[List[Union[str, MedicalEnumeration]], Union[str, MedicalEnumeration]]] = Field(
        None,
        description="Range of acceptable values for a typical patient, when applicable.",
    )
    affectedBy: Any = Field(
        None,
        description="Drugs that affect the test's results.",
    )
    signDetected: Any = Field(
        None,
        description="A sign detected by the test.",
    )
    usedToDiagnose: Any = Field(
        None,
        description="A condition the test is used to diagnose.",
    )
    locals().update({"@type": Field("MedicalTest", const=True)})


MedicalTest.update_forward_refs()
