from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit527(USNonprofitType):
    """Nonprofit527: Non-profit type referring to Political organizations.

    See https://schema.org/Nonprofit527.

    """
    type_: str = Field("Nonprofit527", const=True, alias='@type')
    

Nonprofit527.update_forward_refs()
