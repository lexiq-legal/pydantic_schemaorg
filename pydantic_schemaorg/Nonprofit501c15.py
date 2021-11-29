from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c15(USNonprofitType):
    """Nonprofit501c15: Non-profit type referring to Mutual Insurance Companies or Associations.

    See https://schema.org/Nonprofit501c15.

    """

    locals().update({"@type": Field("Nonprofit501c15", const=True)})


Nonprofit501c15.update_forward_refs()
