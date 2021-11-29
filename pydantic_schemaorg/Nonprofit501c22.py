from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c22(USNonprofitType):
    """Nonprofit501c22: Non-profit type referring to Withdrawal Liability Payment Funds.

    See https://schema.org/Nonprofit501c22.

    """

    locals().update({"@type": Field("Nonprofit501c22", const=True)})


Nonprofit501c22.update_forward_refs()
