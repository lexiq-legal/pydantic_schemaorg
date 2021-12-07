from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c8(USNonprofitType):
    """Nonprofit501c8: Non-profit type referring to Fraternal Beneficiary Societies and"
     "Associations.

    See https://schema.org/Nonprofit501c8.

    """
    type_: str = Field("Nonprofit501c8", const=True, alias='@type')
    

Nonprofit501c8.update_forward_refs()
