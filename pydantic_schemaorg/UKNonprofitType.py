from pydantic import Field
from pydantic_schemaorg.NonprofitType import NonprofitType


class UKNonprofitType(NonprofitType):
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom.

    See https://schema.org/UKNonprofitType.

    """
    type_: str = Field("UKNonprofitType", const=True, alias='@type')
    

UKNonprofitType.update_forward_refs()
