from pydantic import Field
from pydantic_schemaorg.NonprofitType import NonprofitType


class NLNonprofitType(NonprofitType):
    """NLNonprofitType: Non-profit organization type originating from the Netherlands.

    See https://schema.org/NLNonprofitType.

    """

    locals().update({"@type": Field("NLNonprofitType", const=True)})


NLNonprofitType.update_forward_refs()
