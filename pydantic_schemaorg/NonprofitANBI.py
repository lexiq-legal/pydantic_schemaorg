from pydantic import Field
from pydantic_schemaorg.NLNonprofitType import NLNonprofitType


class NonprofitANBI(NLNonprofitType):
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

    See https://schema.org/NonprofitANBI.

    """

    locals().update({"@type": Field("NonprofitANBI", const=True)})


NonprofitANBI.update_forward_refs()
