from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class PaidLeave(GovernmentBenefitsType):
    """PaidLeave: this is a benefit for paid leave.

    See: https://schema.org/PaidLeave
    Model depth: 5
    """
    type_: str = Field("PaidLeave", alias='@type')
    

