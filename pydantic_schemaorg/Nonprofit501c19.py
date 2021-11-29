from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c19(USNonprofitType):
    """Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present"
     "Members of the Armed Forces.

    See https://schema.org/Nonprofit501c19.

    """

    locals().update({"@type": Field("Nonprofit501c19", const=True)})


Nonprofit501c19.update_forward_refs()
