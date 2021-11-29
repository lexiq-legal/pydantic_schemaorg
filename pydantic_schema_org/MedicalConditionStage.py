from pydantic import Field
from decimal import Decimal
from typing import Any, Optional, Union, List
from pydantic_schema_org.MedicalIntangible import MedicalIntangible


class MedicalConditionStage(MedicalIntangible):
    """A stage of a medical condition, such as 'Stage IIIa'.

    See https://schema.org/MedicalConditionStage.

    """

    stageAsNumber: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The stage represented as a number, e.g. 3.",
    )
    subStageSuffix: Optional[Union[List[str], str]] = Field(
        None,
        description="The substage, e.g. 'a' for Stage IIIa.",
    )
    locals().update({"@type": Field("MedicalConditionStage", const=True)})


MedicalConditionStage.update_forward_refs()
