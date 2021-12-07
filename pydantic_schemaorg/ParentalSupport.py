from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class ParentalSupport(GovernmentBenefitsType):
    """ParentalSupport: this is a benefit for parental support.

    See https://schema.org/ParentalSupport.

    """
    type_: str = Field("ParentalSupport", const=True, alias='@type')
    

ParentalSupport.update_forward_refs()
