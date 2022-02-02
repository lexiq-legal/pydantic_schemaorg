from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.MedicalRiskEstimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """A simple system that adds up the number of risk factors to yield a score that is associated"
     "with prognosis, e.g. CHAD score, TIMI risk score.

    See: https://schema.org/MedicalRiskScore
    Model depth: 4
    """
    type_: str = Field("MedicalRiskScore", alias='@type')
    algorithm: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The algorithm or rules to follow to compute the score.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
