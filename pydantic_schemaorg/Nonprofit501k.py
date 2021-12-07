from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501k(USNonprofitType):
    """Nonprofit501k: Non-profit type referring to Child Care Organizations.

    See https://schema.org/Nonprofit501k.

    """
    type_: str = Field("Nonprofit501k", const=True, alias='@type')
    

Nonprofit501k.update_forward_refs()
