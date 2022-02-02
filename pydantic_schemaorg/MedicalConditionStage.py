from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalConditionStage(MedicalIntangible):
    """A stage of a medical condition, such as 'Stage IIIa'.

    See: https://schema.org/MedicalConditionStage
    Model depth: 4
    """
    type_: str = Field("MedicalConditionStage", alias='@type')
    stageAsNumber: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The stage represented as a number, e.g. 3.",
    )
    subStageSuffix: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The substage, e.g. 'a' for Stage IIIa.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
