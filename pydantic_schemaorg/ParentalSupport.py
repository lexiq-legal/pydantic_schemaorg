from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class ParentalSupport(GovernmentBenefitsType):
    """ParentalSupport: this is a benefit for parental support.

    See https://schema.org/ParentalSupport.

    """

    locals().update({"@type": Field("ParentalSupport", const=True)})


ParentalSupport.update_forward_refs()
