from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalRiskEstimator import MedicalRiskEstimator


class MedicalRiskCalculator(MedicalRiskEstimator):
    """A complex mathematical calculation requiring an online calculator, used to assess"
     "prognosis. Note: use the url property of Thing to record any URLs for online calculators.

    See: https://schema.org/MedicalRiskCalculator
    Model depth: 4
    """
    type_: str = Field("MedicalRiskCalculator", alias='@type')
    

