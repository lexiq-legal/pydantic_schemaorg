from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c6(USNonprofitType):
    """Nonprofit501c6: Non-profit type referring to Business Leagues, Chambers of Commerce,"
     "Real Estate Boards.

    See https://schema.org/Nonprofit501c6.

    """

    locals().update({"@type": Field("Nonprofit501c6", const=True)})


Nonprofit501c6.update_forward_refs()
