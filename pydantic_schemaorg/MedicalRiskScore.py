from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalRiskEstimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """A simple system that adds up the number of risk factors to yield a score that is associated"
     "with prognosis, e.g. CHAD score, TIMI risk score.

    See: https://schema.org/MedicalRiskScore
    Model depth: 4
    """
    type_: str = Field(default="MedicalRiskScore", alias='@type', const=True)
    algorithm: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The algorithm or rules to follow to compute the score.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
