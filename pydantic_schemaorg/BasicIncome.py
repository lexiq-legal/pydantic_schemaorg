from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class BasicIncome(GovernmentBenefitsType):
    """BasicIncome: this is a benefit for basic income.

    See: https://schema.org/BasicIncome
    Model depth: 5
    """
    type_: str = Field("BasicIncome", alias='@type')
    

