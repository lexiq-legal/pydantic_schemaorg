from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class UnemploymentSupport(GovernmentBenefitsType):
    """UnemploymentSupport: this is a benefit for unemployment support.

    See: https://schema.org/UnemploymentSupport
    Model depth: 5
    """
    type_: str = Field("UnemploymentSupport", alias='@type')
    

