from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from typing import Any, Union, List, Optional


class MedicalRiskEstimator(MedicalEntity):
    """Any rule set or interactive tool for estimating the risk of developing a complication"
     "or condition.

    See https://schema.org/MedicalRiskEstimator.

    """

    estimatesRiskOf: Optional[Union[List[MedicalEntity], MedicalEntity]] = Field(
        None,
        description="The condition, complication, or symptom whose risk is being estimated.",
    )
    includedRiskFactor: Any = Field(
        None,
        description="A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting"
     "condition.",
    )
    locals().update({"@type": Field("MedicalRiskEstimator", const=True)})


MedicalRiskEstimator.update_forward_refs()
