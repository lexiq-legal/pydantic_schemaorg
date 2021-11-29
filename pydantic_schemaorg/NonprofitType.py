from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class NonprofitType(Enumeration):
    """NonprofitType enumerates several kinds of official non-profit types of which a non-profit"
     "organization can be.

    See https://schema.org/NonprofitType.

    """

    locals().update({"@type": Field("NonprofitType", const=True)})


NonprofitType.update_forward_refs()
