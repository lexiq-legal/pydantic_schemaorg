from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class HealthCare(GovernmentBenefitsType):
    """HealthCare: this is a benefit for health care.

    See: https://schema.org/HealthCare
    Model depth: 5
    """
    type_: str = Field("HealthCare", alias='@type')
    

