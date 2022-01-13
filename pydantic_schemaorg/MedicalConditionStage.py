from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalConditionStage(MedicalIntangible):
    """A stage of a medical condition, such as 'Stage IIIa'.

    See: https://schema.org/MedicalConditionStage
    Model depth: 4
    """

    type_: str = Field("MedicalConditionStage", const=True, alias="@type")
    stageAsNumber: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = (
        Field(
            None,
            description="The stage represented as a number, e.g. 3.",
        )
    )
    subStageSuffix: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The substage, e.g. 'a' for Stage IIIa.",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    MedicalConditionStage.update_forward_refs()
