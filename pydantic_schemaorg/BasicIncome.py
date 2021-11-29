from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class BasicIncome(GovernmentBenefitsType):
    """BasicIncome: this is a benefit for basic income.

    See https://schema.org/BasicIncome.

    """

    locals().update({"@type": Field("BasicIncome", const=True)})


BasicIncome.update_forward_refs()
