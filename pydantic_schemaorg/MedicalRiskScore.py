from pydantic import Field
from typing import List, Optional, Union, Any
from pydantic_schemaorg.MedicalRiskEstimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """A simple system that adds up the number of risk factors to yield a score that is associated"
     "with prognosis, e.g. CHAD score, TIMI risk score.

    See https://schema.org/MedicalRiskScore.

    """

    algorithm: Optional[Union[List[str], str]] = Field(
        None,
        description="The algorithm or rules to follow to compute the score.",
    )
    locals().update({"@type": Field("MedicalRiskScore", const=True)})


MedicalRiskScore.update_forward_refs()
