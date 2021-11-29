from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501d(USNonprofitType):
    """Nonprofit501d: Non-profit type referring to Religious and Apostolic Associations.

    See https://schema.org/Nonprofit501d.

    """

    locals().update({"@type": Field("Nonprofit501d", const=True)})


Nonprofit501d.update_forward_refs()
