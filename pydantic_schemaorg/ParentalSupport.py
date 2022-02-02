from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class ParentalSupport(GovernmentBenefitsType):
    """ParentalSupport: this is a benefit for parental support.

    See: https://schema.org/ParentalSupport
    Model depth: 5
    """
    type_: str = Field("ParentalSupport", alias='@type')
    

