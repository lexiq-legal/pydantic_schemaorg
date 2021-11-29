from pydantic import Field
from pydantic_schemaorg.NonprofitType import NonprofitType


class UKNonprofitType(NonprofitType):
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom.

    See https://schema.org/UKNonprofitType.

    """

    locals().update({"@type": Field("UKNonprofitType", const=True)})


UKNonprofitType.update_forward_refs()
