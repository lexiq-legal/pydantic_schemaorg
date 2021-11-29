from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c12(USNonprofitType):
    """Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations,"
     "Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies.

    See https://schema.org/Nonprofit501c12.

    """

    locals().update({"@type": Field("Nonprofit501c12", const=True)})


Nonprofit501c12.update_forward_refs()
