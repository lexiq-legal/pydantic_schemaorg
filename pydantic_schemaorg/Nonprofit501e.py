from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501e(USNonprofitType):
    """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.

    See https://schema.org/Nonprofit501e.

    """

    locals().update({"@type": Field("Nonprofit501e", const=True)})


Nonprofit501e.update_forward_refs()
