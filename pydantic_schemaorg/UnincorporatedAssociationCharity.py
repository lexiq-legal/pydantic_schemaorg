from pydantic import Field
from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class UnincorporatedAssociationCharity(UKNonprofitType):
    """UnincorporatedAssociationCharity: Non-profit type referring to a charitable company"
     "that is not incorporated (UK).

    See https://schema.org/UnincorporatedAssociationCharity.

    """
    type_: str = Field("UnincorporatedAssociationCharity", const=True, alias='@type')
    

UnincorporatedAssociationCharity.update_forward_refs()
