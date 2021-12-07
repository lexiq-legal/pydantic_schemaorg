from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c24(USNonprofitType):
    """Nonprofit501c24: Non-profit type referring to Section 4049 ERISA Trusts.

    See https://schema.org/Nonprofit501c24.

    """
    type_: str = Field("Nonprofit501c24", const=True, alias='@type')
    

Nonprofit501c24.update_forward_refs()
