from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c11(USNonprofitType):
    """Nonprofit501c11: Non-profit type referring to Teachers' Retirement Fund Associations.

    See https://schema.org/Nonprofit501c11.

    """
    type_: str = Field("Nonprofit501c11", const=True, alias='@type')
    

Nonprofit501c11.update_forward_refs()
