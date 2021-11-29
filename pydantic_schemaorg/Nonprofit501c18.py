from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c18(USNonprofitType):
    """Nonprofit501c18: Non-profit type referring to Employee Funded Pension Trust (created"
     "before 25 June 1959).

    See https://schema.org/Nonprofit501c18.

    """

    locals().update({"@type": Field("Nonprofit501c18", const=True)})


Nonprofit501c18.update_forward_refs()
