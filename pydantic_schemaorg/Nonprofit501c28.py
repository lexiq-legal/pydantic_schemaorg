from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c28(USNonprofitType):
    """Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment"
     "Trusts.

    See https://schema.org/Nonprofit501c28.

    """
    type_: str = Field("Nonprofit501c28", const=True, alias='@type')
    

Nonprofit501c28.update_forward_refs()
