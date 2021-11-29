from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit527(USNonprofitType):
    """Nonprofit527: Non-profit type referring to Political organizations.

    See https://schema.org/Nonprofit527.

    """

    locals().update({"@type": Field("Nonprofit527", const=True)})


Nonprofit527.update_forward_refs()
