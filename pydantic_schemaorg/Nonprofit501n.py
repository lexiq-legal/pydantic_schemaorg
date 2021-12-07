from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501n(USNonprofitType):
    """Nonprofit501n: Non-profit type referring to Charitable Risk Pools.

    See https://schema.org/Nonprofit501n.

    """
    type_: str = Field("Nonprofit501n", const=True, alias='@type')
    

Nonprofit501n.update_forward_refs()
