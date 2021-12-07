from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class PaidLeave(GovernmentBenefitsType):
    """PaidLeave: this is a benefit for paid leave.

    See https://schema.org/PaidLeave.

    """
    type_: str = Field("PaidLeave", const=True, alias='@type')
    

PaidLeave.update_forward_refs()
