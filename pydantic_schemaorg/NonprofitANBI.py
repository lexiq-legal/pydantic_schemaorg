from pydantic import Field
from pydantic_schemaorg.NLNonprofitType import NLNonprofitType


class NonprofitANBI(NLNonprofitType):
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

    See https://schema.org/NonprofitANBI.

    """
    type_: str = Field("NonprofitANBI", const=True, alias='@type')
    

NonprofitANBI.update_forward_refs()
