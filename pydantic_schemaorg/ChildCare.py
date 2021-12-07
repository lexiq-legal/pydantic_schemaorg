from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ChildCare(LocalBusiness):
    """A Childcare center.

    See https://schema.org/ChildCare.

    """
    type_: str = Field("ChildCare", const=True, alias='@type')
    

ChildCare.update_forward_refs()
