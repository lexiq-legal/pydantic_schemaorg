from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c14(USNonprofitType):
    """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual"
     "Reserve Funds.

    See https://schema.org/Nonprofit501c14.

    """

    locals().update({"@type": Field("Nonprofit501c14", const=True)})


Nonprofit501c14.update_forward_refs()
