from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class BusinessSupport(GovernmentBenefitsType):
    """BusinessSupport: this is a benefit for supporting businesses.

    See: https://schema.org/BusinessSupport
    Model depth: 5
    """
    type_: str = Field("BusinessSupport", alias='@type')
    

