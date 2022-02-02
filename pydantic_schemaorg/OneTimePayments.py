from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class OneTimePayments(GovernmentBenefitsType):
    """OneTimePayments: this is a benefit for one-time payments for individuals.

    See: https://schema.org/OneTimePayments
    Model depth: 5
    """
    type_: str = Field("OneTimePayments", alias='@type')
    

