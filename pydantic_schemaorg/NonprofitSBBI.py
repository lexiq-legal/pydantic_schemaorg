from pydantic import Field
from pydantic_schemaorg.NLNonprofitType import NLNonprofitType


class NonprofitSBBI(NLNonprofitType):
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution"
     "(NL).

    See https://schema.org/NonprofitSBBI.

    """
    type_: str = Field("NonprofitSBBI", const=True, alias='@type')
    

NonprofitSBBI.update_forward_refs()
