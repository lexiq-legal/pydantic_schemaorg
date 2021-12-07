from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c20(USNonprofitType):
    """Nonprofit501c20: Non-profit type referring to Group Legal Services Plan Organizations.

    See https://schema.org/Nonprofit501c20.

    """
    type_: str = Field("Nonprofit501c20", const=True, alias='@type')
    

Nonprofit501c20.update_forward_refs()
