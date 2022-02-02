from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalRiskEstimator(MedicalEntity):
    """Any rule set or interactive tool for estimating the risk of developing a complication"
     "or condition.

    See: https://schema.org/MedicalRiskEstimator
    Model depth: 3
    """
    type_: str = Field("MedicalRiskEstimator", alias='@type')
    estimatesRiskOf: Optional[Union[List[Union['MedicalEntity', str]], 'MedicalEntity', str]] = Field(
        None,
        description="The condition, complication, or symptom whose risk is being estimated.",
    )
    includedRiskFactor: Optional[Union[List[Union['MedicalRiskFactor', str]], 'MedicalRiskFactor', str]] = Field(
        None,
        description="A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting"
     "condition.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
    from pydantic_schemaorg.MedicalRiskFactor import MedicalRiskFactor
