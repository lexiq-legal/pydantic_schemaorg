from pydantic import Field
from pydantic_schemaorg.NonprofitType import NonprofitType


class USNonprofitType(NonprofitType):
    """USNonprofitType: Non-profit organization type originating from the United States.

    See https://schema.org/USNonprofitType.

    """

    locals().update({"@type": Field("USNonprofitType", const=True)})


USNonprofitType.update_forward_refs()
