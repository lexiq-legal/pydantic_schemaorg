from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class GovernmentBenefitsType(Enumeration):
    """GovernmentBenefitsType enumerates several kinds of government benefits to support"
     "the COVID-19 situation. Note that this structure may not capture all benefits offered.

    See https://schema.org/GovernmentBenefitsType.

    """

    locals().update({"@type": Field("GovernmentBenefitsType", const=True)})


GovernmentBenefitsType.update_forward_refs()
