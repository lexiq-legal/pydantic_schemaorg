from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from typing import List, Optional, Union
from pydantic_schemaorg.MedicalRiskFactor import MedicalRiskFactor


class MedicalRiskEstimator(MedicalEntity):
    """Any rule set or interactive tool for estimating the risk of developing a complication"
     "or condition.

    See https://schema.org/MedicalRiskEstimator.

    """
    type_: str = Field("MedicalRiskEstimator", const=True, alias='@type')
    estimatesRiskOf: Optional[Union[List[Union[MedicalEntity, str]], Union[MedicalEntity, str]]] = Field(
        None,
        description="The condition, complication, or symptom whose risk is being estimated.",
    )
    includedRiskFactor: Optional[Union[List[Union[MedicalRiskFactor, str]], Union[MedicalRiskFactor, str]]] = Field(
        None,
        description="A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting"
     "condition.",
    )
    

MedicalRiskEstimator.update_forward_refs()
