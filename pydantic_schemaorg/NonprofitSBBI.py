from pydantic import Field
from pydantic_schemaorg.NLNonprofitType import NLNonprofitType


class NonprofitSBBI(NLNonprofitType):
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution"
     "(NL).

    See https://schema.org/NonprofitSBBI.

    """

    locals().update({"@type": Field("NonprofitSBBI", const=True)})


NonprofitSBBI.update_forward_refs()
