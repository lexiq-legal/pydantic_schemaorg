from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class UnemploymentSupport(GovernmentBenefitsType):
    """UnemploymentSupport: this is a benefit for unemployment support.

    See https://schema.org/UnemploymentSupport.

    """
    type_: str = Field("UnemploymentSupport", const=True, alias='@type')
    

UnemploymentSupport.update_forward_refs()
