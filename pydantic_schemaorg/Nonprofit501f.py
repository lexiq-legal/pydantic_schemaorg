from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501f(USNonprofitType):
    """Nonprofit501f: Non-profit type referring to Cooperative Service Organizations.

    See https://schema.org/Nonprofit501f.

    """

    locals().update({"@type": Field("Nonprofit501f", const=True)})


Nonprofit501f.update_forward_refs()
