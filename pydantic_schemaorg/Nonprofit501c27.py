from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c27(USNonprofitType):
    """Nonprofit501c27: Non-profit type referring to State-Sponsored Workers' Compensation"
     "Reinsurance Organizations.

    See https://schema.org/Nonprofit501c27.

    """
    type_: str = Field("Nonprofit501c27", const=True, alias='@type')
    

Nonprofit501c27.update_forward_refs()
