from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501q(USNonprofitType):
    """Nonprofit501q: Non-profit type referring to Credit Counseling Organizations.

    See https://schema.org/Nonprofit501q.

    """

    locals().update({"@type": Field("Nonprofit501q", const=True)})


Nonprofit501q.update_forward_refs()
