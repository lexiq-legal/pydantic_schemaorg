from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c23(USNonprofitType):
    """Nonprofit501c23: Non-profit type referring to Veterans Organizations.

    See https://schema.org/Nonprofit501c23.

    """
    type_: str = Field("Nonprofit501c23", const=True, alias='@type')
    

Nonprofit501c23.update_forward_refs()
