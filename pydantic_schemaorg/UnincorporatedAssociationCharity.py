from pydantic import Field
from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class UnincorporatedAssociationCharity(UKNonprofitType):
    """UnincorporatedAssociationCharity: Non-profit type referring to a charitable company"
     "that is not incorporated (UK).

    See https://schema.org/UnincorporatedAssociationCharity.

    """

    locals().update({"@type": Field("UnincorporatedAssociationCharity", const=True)})


UnincorporatedAssociationCharity.update_forward_refs()
