from pydantic import Field
from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class CharitableIncorporatedOrganization(UKNonprofitType):
    """CharitableIncorporatedOrganization: Non-profit type referring to a Charitable"
     "Incorporated Organization (UK).

    See https://schema.org/CharitableIncorporatedOrganization.

    """
    type_: str = Field("CharitableIncorporatedOrganization", const=True, alias='@type')
    

CharitableIncorporatedOrganization.update_forward_refs()
