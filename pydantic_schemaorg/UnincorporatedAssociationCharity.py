from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class UnincorporatedAssociationCharity(UKNonprofitType):
    """UnincorporatedAssociationCharity: Non-profit type referring to a charitable company"
     "that is not incorporated (UK).

    See: https://schema.org/UnincorporatedAssociationCharity
    Model depth: 6
    """

    type_: str = Field("UnincorporatedAssociationCharity", const=True, alias="@type")


if TYPE_CHECKING:

    UnincorporatedAssociationCharity.update_forward_refs()
