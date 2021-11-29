from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class HealthCare(GovernmentBenefitsType):
    """HealthCare: this is a benefit for health care.

    See https://schema.org/HealthCare.

    """

    locals().update({"@type": Field("HealthCare", const=True)})


HealthCare.update_forward_refs()
