from pydantic import Field
from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class CharitableIncorporatedOrganization(UKNonprofitType):
    """CharitableIncorporatedOrganization: Non-profit type referring to a Charitable"
     "Incorporated Organization (UK).

    See https://schema.org/CharitableIncorporatedOrganization.

    """

    locals().update({"@type": Field("CharitableIncorporatedOrganization", const=True)})


CharitableIncorporatedOrganization.update_forward_refs()
