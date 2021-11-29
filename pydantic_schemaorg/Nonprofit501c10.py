from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c10(USNonprofitType):
    """Nonprofit501c10: Non-profit type referring to Domestic Fraternal Societies and Associations.

    See https://schema.org/Nonprofit501c10.

    """

    locals().update({"@type": Field("Nonprofit501c10", const=True)})


Nonprofit501c10.update_forward_refs()
