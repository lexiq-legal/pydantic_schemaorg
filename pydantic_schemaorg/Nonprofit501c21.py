from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c21(USNonprofitType):
    """Nonprofit501c21: Non-profit type referring to Black Lung Benefit Trusts.

    See https://schema.org/Nonprofit501c21.

    """

    locals().update({"@type": Field("Nonprofit501c21", const=True)})


Nonprofit501c21.update_forward_refs()
