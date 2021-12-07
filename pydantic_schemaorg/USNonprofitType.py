from pydantic import Field
from pydantic_schemaorg.NonprofitType import NonprofitType


class USNonprofitType(NonprofitType):
    """USNonprofitType: Non-profit organization type originating from the United States.

    See https://schema.org/USNonprofitType.

    """
    type_: str = Field("USNonprofitType", const=True, alias='@type')
    

USNonprofitType.update_forward_refs()
