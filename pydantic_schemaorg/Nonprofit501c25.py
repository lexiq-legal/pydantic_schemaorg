from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c25(USNonprofitType):
    """Nonprofit501c25: Non-profit type referring to Real Property Title-Holding Corporations"
     "or Trusts with Multiple Parents.

    See https://schema.org/Nonprofit501c25.

    """

    locals().update({"@type": Field("Nonprofit501c25", const=True)})


Nonprofit501c25.update_forward_refs()
