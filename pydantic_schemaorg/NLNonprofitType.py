from pydantic import Field
from pydantic_schemaorg.NonprofitType import NonprofitType


class NLNonprofitType(NonprofitType):
    """NLNonprofitType: Non-profit organization type originating from the Netherlands.

    See https://schema.org/NLNonprofitType.

    """
    type_: str = Field("NLNonprofitType", const=True, alias='@type')
    

NLNonprofitType.update_forward_refs()
