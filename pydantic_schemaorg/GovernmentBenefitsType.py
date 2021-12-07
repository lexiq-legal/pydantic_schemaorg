from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class GovernmentBenefitsType(Enumeration):
    """GovernmentBenefitsType enumerates several kinds of government benefits to support"
     "the COVID-19 situation. Note that this structure may not capture all benefits offered.

    See https://schema.org/GovernmentBenefitsType.

    """
    type_: str = Field("GovernmentBenefitsType", const=True, alias='@type')
    

GovernmentBenefitsType.update_forward_refs()
