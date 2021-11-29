from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c20(USNonprofitType):
    """Nonprofit501c20: Non-profit type referring to Group Legal Services Plan Organizations.

    See https://schema.org/Nonprofit501c20.

    """

    locals().update({"@type": Field("Nonprofit501c20", const=True)})


Nonprofit501c20.update_forward_refs()
