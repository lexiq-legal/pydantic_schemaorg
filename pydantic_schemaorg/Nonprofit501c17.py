from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c17(USNonprofitType):
    """Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit"
     "Trusts.

    See https://schema.org/Nonprofit501c17.

    """
    type_: str = Field("Nonprofit501c17", const=True, alias='@type')
    

Nonprofit501c17.update_forward_refs()
