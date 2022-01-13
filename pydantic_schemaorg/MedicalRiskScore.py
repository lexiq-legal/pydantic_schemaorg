from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.MedicalRiskEstimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """A simple system that adds up the number of risk factors to yield a score that is associated"
     "with prognosis, e.g. CHAD score, TIMI risk score.

    See: https://schema.org/MedicalRiskScore
    Model depth: 4
    """

    type_: str = Field("MedicalRiskScore", const=True, alias="@type")
    algorithm: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The algorithm or rules to follow to compute the score.",
    )


if TYPE_CHECKING:

    MedicalRiskScore.update_forward_refs()
