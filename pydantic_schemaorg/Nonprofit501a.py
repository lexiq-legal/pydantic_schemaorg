from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501a(USNonprofitType):
    """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.

    See https://schema.org/Nonprofit501a.

    """

    locals().update({"@type": Field("Nonprofit501a", const=True)})


Nonprofit501a.update_forward_refs()
