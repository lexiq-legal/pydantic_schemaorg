from pydantic import Field
from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class UKTrust(UKNonprofitType):
    """UKTrust: Non-profit type referring to a UK trust.

    See https://schema.org/UKTrust.

    """

    locals().update({"@type": Field("UKTrust", const=True)})


UKTrust.update_forward_refs()
