from pydantic import Field
from decimal import Decimal
from typing import List, Optional, Any, Union
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalConditionStage(MedicalIntangible):
    """A stage of a medical condition, such as 'Stage IIIa'.

    See https://schema.org/MedicalConditionStage.

    """
    type_: str = Field("MedicalConditionStage", const=True, alias='@type')
    stageAsNumber: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The stage represented as a number, e.g. 3.",
    )
    subStageSuffix: Optional[Union[List[str], str]] = Field(
        None,
        description="The substage, e.g. 'a' for Stage IIIa.",
    )
    

MedicalConditionStage.update_forward_refs()
