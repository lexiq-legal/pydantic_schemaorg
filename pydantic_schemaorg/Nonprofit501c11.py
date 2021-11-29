from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c11(USNonprofitType):
    """Nonprofit501c11: Non-profit type referring to Teachers' Retirement Fund Associations.

    See https://schema.org/Nonprofit501c11.

    """

    locals().update({"@type": Field("Nonprofit501c11", const=True)})


Nonprofit501c11.update_forward_refs()
