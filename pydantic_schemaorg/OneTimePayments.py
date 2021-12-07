from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class OneTimePayments(GovernmentBenefitsType):
    """OneTimePayments: this is a benefit for one-time payments for individuals.

    See https://schema.org/OneTimePayments.

    """
    type_: str = Field("OneTimePayments", const=True, alias='@type')
    

OneTimePayments.update_forward_refs()
