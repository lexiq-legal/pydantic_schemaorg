from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class AutomotiveBusiness(LocalBusiness):
    """Car repair, sales, or parts.

    See https://schema.org/AutomotiveBusiness.

    """
    type_: str = Field("AutomotiveBusiness", const=True, alias='@type')
    

AutomotiveBusiness.update_forward_refs()
