from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class BasicIncome(GovernmentBenefitsType):
    """BasicIncome: this is a benefit for basic income.

    See https://schema.org/BasicIncome.

    """
    type_: str = Field("BasicIncome", const=True, alias='@type')
    

BasicIncome.update_forward_refs()
