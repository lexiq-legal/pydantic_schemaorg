from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class DisabilitySupport(GovernmentBenefitsType):
    """DisabilitySupport: this is a benefit for disability support.

    See: https://schema.org/DisabilitySupport
    Model depth: 5
    """
    type_: str = Field("DisabilitySupport", alias='@type')
    

