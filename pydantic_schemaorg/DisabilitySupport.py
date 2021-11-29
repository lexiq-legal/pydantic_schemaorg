from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class DisabilitySupport(GovernmentBenefitsType):
    """DisabilitySupport: this is a benefit for disability support.

    See https://schema.org/DisabilitySupport.

    """

    locals().update({"@type": Field("DisabilitySupport", const=True)})


DisabilitySupport.update_forward_refs()
