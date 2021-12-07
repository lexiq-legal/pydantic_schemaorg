from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class BusinessSupport(GovernmentBenefitsType):
    """BusinessSupport: this is a benefit for supporting businesses.

    See https://schema.org/BusinessSupport.

    """
    type_: str = Field("BusinessSupport", const=True, alias='@type')
    

BusinessSupport.update_forward_refs()
