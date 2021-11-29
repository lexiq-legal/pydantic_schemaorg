from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c27(USNonprofitType):
    """Nonprofit501c27: Non-profit type referring to State-Sponsored Workers' Compensation"
     "Reinsurance Organizations.

    See https://schema.org/Nonprofit501c27.

    """

    locals().update({"@type": Field("Nonprofit501c27", const=True)})


Nonprofit501c27.update_forward_refs()
