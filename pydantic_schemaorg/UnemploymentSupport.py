from pydantic import Field
from pydantic_schemaorg.GovernmentBenefitsType import GovernmentBenefitsType


class UnemploymentSupport(GovernmentBenefitsType):
    """UnemploymentSupport: this is a benefit for unemployment support.

    See https://schema.org/UnemploymentSupport.

    """

    locals().update({"@type": Field("UnemploymentSupport", const=True)})


UnemploymentSupport.update_forward_refs()
