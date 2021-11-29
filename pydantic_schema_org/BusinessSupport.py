from pydantic import Field
from pydantic_schema_org.GovernmentBenefitsType import GovernmentBenefitsType


class BusinessSupport(GovernmentBenefitsType):
    """BusinessSupport: this is a benefit for supporting businesses.

    See https://schema.org/BusinessSupport.

    """

    locals().update({"@type": Field("BusinessSupport", const=True)})


BusinessSupport.update_forward_refs()
